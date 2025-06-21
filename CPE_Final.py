from menu_dict import menu
import time
import random
from printreceipt import print_receipt

business_name = "Traveler's Tavern"
order_number = random.randint(1000, 9999)
cashier = random.choice(['Diluc', 'Charles', 'Sara', 'Xiangling', 'Smiley Yanxiao'])


print('============================================')
intro = """
\033[33mGood day! 👨‍🎓 We are Group 1 of Section A141, presenting to you today for our CPE001L Final Presentation 🖥

Meet the team:
DACUYCUY, Gene Marc
PLAYDA, Kherk Reign Kenji
ROYO, Jahna Raya

DESIGNING A SELF-ORDERING KIOSK PYTHON PROGRAM FOR ENHANCING CUSTOMER EXPERIENCE AT TRAVELER'S TAVERN 
\033[0m"""
print(intro)
print('============================================\n')

# Start the program by displaying a welcome message and asking the customer to enter their name.
print("Ad Astra Abyssosque!✨ Welcome to Traveler's Tavern!")
customerName = str(input("Customer Name:"))
print("Hello, " + customerName + "! Are you dining in or taking out?")

# Then the computer asks if they are dining in or taking out.
# It will repeat the question 3 times if the customer inputs an invalid option.
# If the customer enters an invalid dining option after 3 attempts, there will be a 10-second timer before using again.

num_invalid_options = 0

while True:
    option = input("Enter 'D' for dine-in or 'T' for takeout:  ")
    if option.upper() not in ['D', 'T']:
        num_invalid_options += 1
        print("Invalid choice.")
        if num_invalid_options == 3:
            print("Too many invalid choices. Please wait 10 seconds before trying again.")
            time.sleep(10)
            num_invalid_options = 0
        continue
    else:
        break

if option.upper() == 'D' or 'Dine-In':
    print("You have selected dine-in.")
elif option.upper() == 'T' or 'Takeout':
    print("You have selected takeout.")

# This is where the ordering of the menu starts.
for category, items in menu.items():
    print(f"\n{category}:")
    for item_code, item_info in items.items():
        name = item_info['name']
        price = item_info['price']
        print(f"{item_code}: {name} - PHP {price}")

order_list = []
while True:
    order = input("\nPlease enter the item code of your order(s): ")
    order_list.extend(order.split("," and ", "))
    order_more = input("Do you want to add more orders? (y/n) ")
    if order_more.lower() != "y":
        break

total_cost = 0
for item_code in order_list:
    item_code = item_code.upper()
    for category, items in menu.items():
        item_details = items.get(item_code)
        if item_details:
            print('')
            print(f"{item_details['name']} - PHP {item_details['price']:.2f}")
            total_cost += item_details['price']
            break
    else:
        pass
print('')
print(f"Total cost: PHP {total_cost:.2f}")

# This section will ask the payment option of the customer

payment_method = input("How do you want to pay? (cash/e-money) ")
if payment_method.lower() == "e-money":
    print("Please scan the QR code and proceed to the cashier.")
    # simulate QR code generation and scanning
    qr_code = """
        #######
        #######
        #######
    """
    print(qr_code)
    done = input("Type 'done' once you have scanned the QR code: ")
    if done.lower() == 'done':
        print("Payment received. Thank you!")
        cash_received = float(input("Enter amount of cash: PHP "))
        change = cash_received - total_cost
    else:
        print("Payment not received. Please ask assistance to our staff.")

# If user uses the cash choice, a cashier transaction simulation is made.

else:
    print("Please proceed to the cashier.")
    while True:
        try:
            cash_received = float(input("Enter amount of cash: PHP "))

            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

change = cash_received - total_cost

if change < 0:
    print("Insufficient payment. Please pay the correct amount.")
else:
    print(f"\n Change: PHP {change:.2f}. Thank you!")
# printing the receipt
print_receipt(order_number, customerName, cashier, option, payment_method, order_list, total_cost, cash_received,
              change)
print("\n Please wait as we prepare your meal! ✨")