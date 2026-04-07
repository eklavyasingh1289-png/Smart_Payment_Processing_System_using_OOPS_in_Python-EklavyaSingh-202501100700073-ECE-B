from abc import ABC, abstractmethod
class Payment(ABC):
    def __init__(self,user_name):
        self.user_name = user_name
        self.original = 0
        self.amount = 0

    def pay(self,amount):
        print()
    
    def generate_receipt(self):
        print("\n\n\n")
        print(f"User : {self.user_name}")
        print(f"Original Amount : {self.original}")
        print(f"Final Amount : {self.amount}")
        print("\n\n\n")

class Credit_Card_Payment(Payment):
    def pay(self,amt):
        self.original = amt
        gateway_fee = amt*.02
        gst = gateway_fee*.18
        self.amount = amt + gateway_fee + gst
        self.generate_receipt()

class UPI_Payment(Payment):
    def pay(self,amt):
        self.original = amt
        if(amt>1000):
            self.amount = amt-50
        else:
            self.amount = amt
        self.generate_receipt()
    
class Pay_Pal_Payment(Payment):
    def pay(self,amt):
        self.original = amt
        international_fees = amt*.03
        currency_conversion = 20
        self.amount = amt + international_fees + currency_conversion
        self.generate_receipt()


class Wallet_Payment(Payment):
    def __init__(self, user_name, balance):
        super().__init__(user_name)
        self.balance = balance

    def pay(self, amount):
        self.original_amount = amount        
        if amount > self.balance:
            print(f"Transaction Failed: Insufficient Wallet Balance! (Current: ₹{self.balance})")
        else:
            self.balance -= amount
            self.final_amount = amount
            print(f"Payment successful. Remaining Balance: ₹{self.balance:.2f}")
            self.generate_receipt()

def process_payment(payment_object, amount):
    payment_object.pay(amount)


def main():
    name = input("Enter your name: ")    
    methods = {
        "1": Credit_Card_Payment(name),
        "2": UPI_Payment(name),
        "3": Pay_Pal_Payment(name),
        "4": Wallet_Payment(name, 1000.00)
    }

    while True:
        print("\n\n\n\n1. Credit Card (2% fee + 18% GST on fee)")
        print("2. UPI (₹50 cashback if > ₹1000)")
        print("3. PayPal (3% fee + ₹20 conversion)")
        print("4. Digital Wallet (Current Balance: ₹{:.2f})".format(methods["4"].balance))
        choice = input("\nSelect a payment method (1-5): ")
        if choice in methods:
            try:
                amt = float(input("Enter amount to pay: ₹"))
                if amt <= 0:
                    print("[!] Amount must be positive.")
                    continue
                
                
                process_payment(methods[choice], amt)
                
            except ValueError:
                print("[!] Invalid input. Please enter a numerical amount.")
        else:
            print("[!] Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()