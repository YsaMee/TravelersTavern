import random
from menu_dict import menu

business_name = "Traveler's Tavern"
order_number = random.randint(1000, 9999)
cashier = random.choice(['Diluc', 'Charles', 'Sara', 'Xiangling', 'Smiley Yanxiao'])


def print_receipt(order_number, customer_name, cashier, dining_option, payment_method, order_list, total_cost,
                  cash_received, change):
    with open(f"receipt_{order_number}.txt", "w") as f:
        f.write('---TRAVELER\'S TAVERN---\n')
        f.write('============================================\n')
        f.write('============================================\n')
        f.write(f'Order Number: {order_number}\n')
        f.write('============================================\n')
        f.write(f'Customer Name: {customer_name}\n')
        f.write(f'Cashier: {cashier}\n')
        f.write(f'Dining Option: {dining_option}\n')
        f.write('Order List:\n')
        for item_code in order_list:
            item_code = item_code.upper()
            for category, items in menu.items():
                item_details = items.get(item_code)
                if item_details:
                    f.write(f"{item_details['name']} - PHP {item_details['price']:.2f}\n")
                    break
            else:
                pass
        f.write('\n')
        f.write(f'Total: PHP {total_cost:.2f}\n')
        f.write(f'Payment Method: {payment_method}\n')
        f.write(f'Received Cash: PHP {cash_received:.2f}\n')
        f.write(f'Change: PHP {change:.2f}\n\n')
        f.write('Thank you for dining with us!')
    print(f"Receipt {order_number} has been printed.")
