import requests
import base64
from termcolor import colored
import os

def generate_access_token(client_id, secret_id):
    auth_string = client_id + ":" + secret_id
    encoded_auth_string = base64.b64encode(auth_string.encode("utf-8")).decode("utf-8")
    
    url = "https://api.sandbox.paypal.com/v1/oauth2/token"
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic " + encoded_auth_string
    }
    
    data = {
        "grant_type": "client_credentials"
    }
    
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        access_token = response.json()["access_token"]
        return access_token
    else:
        print("Oops, something went wrong while generating the access token!")
        print(response.json())

def send_money(sender_email, receiver_email, amount, access_token):
    url = "https://api.sandbox.paypal.com/v1/payments/payouts"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + access_token
    }
    
    data = {
        "sender_batch_header": {
            "sender_batch_id": "YOUR_UNIQUE_BATCH_ID",
            "email_subject": "You've received money!"
        },
        "items": [
            {
                "recipient_type": "EMAIL",
                "amount": {
                    "value": amount,
                    "currency": "USD"
                },
                "note": "Enjoy your free money!",
                "receiver": receiver_email,
                "sender_item_id": "ITEM_1"
            }
        ]
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 201:
        print(colored("Money sent successfully!", "green"))
    else:
        print(colored("Oops, something went wrong while sending money!", "red"))
        print(response.json())

def fancy_box(text):
    box_width = len(text) + 4
    print(colored("╔" + "═" * box_width + "╗", "blue"))
    print(colored("║ " + text + " ║", "blue"))
    print(colored("╚" + "═" * box_width + "╝", "blue"))

def manual_money_sender():
    fancy_box(colored("Add Money to PayPal", "yellow"))
    
    # User input for client ID and secret ID
    client_id = input(colored("Enter your PayPal sandbox client ID: ", "cyan"))
    secret_id = input(colored("Enter your PayPal sandbox secret ID: ", "cyan"))
    
    # User input for sender and receiver email
    sender_email = input(colored("Enter the sender's email address: ", "cyan"))
    receiver_email = input(colored("Enter the receiver's email address: ", "cyan"))
    
    amount = input(colored("Enter the amount to send: ", "cyan"))
    
    access_token = generate_access_token(client_id, secret_id)
    send_money(sender_email, receiver_email, amount, access_token)

# Clear the terminal/console screen
os.system("clear" if os.name == "posix" else "cls")

# Loop to continue using the program
while True:
    manual_money_sender()
    choice = input("Do you want to send money again? (y/n): ")
    if choice.lower() != "y":
        break
