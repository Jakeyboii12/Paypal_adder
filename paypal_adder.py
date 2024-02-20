import requests
import json
from colorama import init, Fore
import os

def check_balance(address):
    url = f"https://blockchain.info/address/{address}?format=json"
    response = requests.get(url)
    data = json.loads(response.text)
    final_balance = data['final_balance'] / 100000000

    return final_balance

def withdraw(sender_address, recipient_address, amount, balance):
    # Implement your withdrawal logic here
    # Subtract the amount from the balance
    # Make sure to handle any error conditions or validations
    
    # Example:
    if balance >= amount:
        balance -= amount
        print(f"Withdrew {amount} BTC from {sender_address} to {recipient_address}.")
    else:
        print("Insufficient balance for withdrawal.")

    return balance

def display_logo():
    init()  # Initialize colorama
    logo = f"""
{Fore.RED}     ___  _     _                _     
    |_ _|<_> __| |_ _ __ ___  __| |___ 
     | || | '_ \| _| '_ ` _ \/ _` / -_)
    |___|_|_|_|_|__|_| |_| |_|\__,_\___|{Fore.RESET}

    """
    print(logo)

def restart():
    os.system('clear' if os.name == 'posix' else 'cls')
    main()

def main():
    display_logo()

    sender_address = input("Enter your Bitcoin sender address: ")
    balance = check_balance(sender_address)
    print(f"The balance of {sender_address} is {balance} BTC.")

    recipient_address = input("Enter the recipient Bitcoin address: ")
    withdraw_amount = float(input("Enter the withdrawal amount: "))

    balance = withdraw(sender_address, recipient_address, withdraw_amount, balance)

    print(f"The updated balance of {sender_address} is {balance} BTC.")

# Code execution
if __name__ == "__main__":
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        main()
        input("Press Enter to restart the code...")
