from abc import ABC, abstractmethod
import time
import datetime
import logging
logging.basicConfig(filename='LOG_DATA.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.info("Program started")
print('''
               ***       ***  ********** ***       ********* *********  *************** **********
               ***  ***  ***  *********  ***       ********* *********  *************** *********
               ***  ***  ***  ***        ***       ***       ***   ***  ***   ***   *** ***
               ***  ***  ***  ******     ***       ***       ***   ***  ***   ***   *** ******
               ***  ***  ***  ******     ***       ***       ***   ***  ***   ***   *** ******
               ***  ***  ***  ***        ***       ***       ***   ***  ***   ***   *** ***
               *************  *********  ********* ********* *********  ***   ***   *** *********
               *************  ********** ********* ********* *********  ***         *** **********
               
                                        ************* ***********
                                        ************* ***********
                                             ***      ***     ***
                                             ***      ***     ***
                                             ***      ***     ***                                
                                             ***      ***     ***
                                             ***      ***     ***
                                             ***      ***********
                                             ***      ***********

        ************ *************** ************    ********** ********** ********** **********  *********
        ************ *************** ************    ********** ********** ********** **********  ********
        ****    **** ***   ***   *** ***      ***    ***            ***    ***    *** **      **  *** 
        ****    **** ***   ***   *** ***      ***    ***            ***    ***    *** **      **  ******
        ************ ***   ***   *** ***      ***    **********     ***    ***    *** **********  ******
        ************ ***   ***   *** ***      ***    **********     ***    ***    *** **********  ***
        ***      *** ***   ***   *** ***      ***           ***     ***    ***    *** **     ***  ***
        ***      *** ***   ***   *** ************    **********     ***    ********** **      *** ********
        ***      *** ***         *** ************    **********     ***    ********** **       ** *********

''')

class Product(ABC):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        logging.debug(f"Product created: {self.name}, Price: {self.price}, Quantity: {self.quantity}")

    @abstractmethod
    def __str__(self):
        pass

class Item(Product):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def __add__(self, other):
        if isinstance(other, int):
            return self.price + other
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Item' and {}".format(type(other).__name__))

    def __sub__(self, other):
        if isinstance(other, int):
            return self.price - other
        else:
            raise TypeError("Unsupported operand type(s) for -: 'Item' and {}".format(type(other).__name__))

    def __str__(self):
        return f"Item: {self.name}, Price: ${self.price}, Quantity: {self.quantity}"
 
class Menu:
    def __init__(self):
        self.items = {
            1: Item("Laptop", 1000, 50),
            2: Item("Smartphone", 800, 50),
            3: Item("Headphones", 150, 50),
            4: Item("Keyboard", 200, 50),
            5: Item("Mouse", 80, 50),
            6: Item("Tablet", 700, 50),
            7: Item("Stylus", 30, 50),
            8: Item("Graphic tablet", 125, 50),
            9: Item("Projector", 300, 50),
            10: Item("Backpack", 50, 50)
        }
        logging.info("Menu initialized with items.")

    def display_menu(self):
        # Function to display the shopping menu
        logging.info("Displaying menu")
        print("\nAvailable Items:")
        print("+------+-------------------+-----------------+------------+")
        print("| No.  | Item              | Price ($)       | Available  |")
        print("+------+-------------------+-----------------+------------+")
        for key, item in self.items.items():
            print(f"| {key:<4} | {item.name:<18} | ${item.price:<15} | {item.quantity:<10} |")
        print("+------+-------------------+-----------------+------------+")

class ShoppingCart(ABC):
    def __init__(self):
        self.cart = []
        logging.info("Shopping cart initialized.")

    @abstractmethod
    def add_to_cart(self, item, quantity):
        pass

    @abstractmethod
    def remove_from_cart(self, item_name):
        pass

    @abstractmethod
    def view_cart(self):
        pass

    @abstractmethod
    def checkout(self, username):
        pass
class UserShoppingCart(ShoppingCart):
    def __init__(self):
        super().__init__()

    def add_to_cart(self, item, quantity):
        while True:
            if quantity == 0:
                print("Quantity cannot be zero. Please enter a valid quantity.")
                logging.warning("Attempted to add zero quantity to the cart.")
                quantity_str = input(f"Enter the quantity of {item.name}: ")
                if not quantity_str.isdigit():
                    print("Invalid input. Please enter a valid quantity.")
                    continue
                quantity = int(quantity_str)
                continue
            if quantity > item.quantity:
                print(f"Sorry, only {item.quantity} {item.name} available.")
                logging.warning(f"Attempted to add more {item.name} than available.")
                quantity_str = input(f"Enter the quantity of {item.name}: ")
                if not quantity_str.isdigit():
                    print("Invalid input. Please enter a valid quantity.")
                    continue
                quantity = int(quantity_str)
                continue

            self.cart.append({"item": item, "quantity": quantity})
            item.quantity -= quantity
            print(f"{quantity} {item.name} added to the cart.")
            logging.info(f"Added {quantity} {item.name} to the cart.")
            break

    def view_cart(self):
        logging.info("Viewing cart")
        print("\nShopping Cart:")
        if not self.cart:
            print("Your cart is empty.")
            logging.info("Cart is empty.")
        else:
            total_price = 0
            for idx, cart_item in enumerate(self.cart, start=1):
                item = cart_item['item']
                subtotal = item.price * cart_item['quantity']
                total_price += subtotal
                print(f"{idx}. {item.name} - ${item.price} each (Quantity: {cart_item['quantity']}) - Subtotal: ${subtotal}")
            print(f"Total Price: ${total_price}")
            logging.info(f"Total price of cart: ${total_price}")

    def remove_from_cart(self, item_name):
        logging.info(f"Attempting to remove {item_name} from cart")

        found_item = None
        for cart_item in self.cart:
            if cart_item['item'].name.lower() == item_name.lower():
                found_item = cart_item
                break

        if found_item:
            while True:
                remove_quantity_str = input(f"How many {item_name} do you want to remove from the cart? ")
                if not remove_quantity_str.isdigit():
                    print("Invalid input. Please enter a valid quantity.")
                    continue
                remove_quantity = int(remove_quantity_str)
                if remove_quantity <= 0:
                    print("Quantity must be a positive integer. Please try again.")
                    continue

                if remove_quantity >= found_item['quantity']:
                    self.cart.remove(found_item)
                    found_item['item'].quantity += found_item['quantity']
                    print(f"All {found_item['quantity']} {item_name} removed from the cart.")
                    logging.info(f"Removed all {found_item['quantity']} {item_name} from the cart.")
                else:
                    found_item['quantity'] -= remove_quantity
                    found_item['item'].quantity += remove_quantity
                    print(f"{remove_quantity} {item_name} removed from the cart.")
                    logging.info(f"Removed {remove_quantity} {item_name} from the cart.")
                break
        else:
            print(f"{item_name} not found in the cart.")
            logging.warning(f"{item_name} not found in the cart.")
    def checkout(self, username):
        logging.info(f"Checking out for user {username}")
        print("\nCheckout - Total Bill:")
        total_bill = sum(cart_item['item'].price * cart_item['quantity'] for cart_item in self.cart)
        for cart_item in self.cart:
            print(f"{cart_item['quantity']} {cart_item['item'].name} - ${cart_item['item'].price} each")
        print('\n')
        print(f"Total: ${total_bill}")
        print("\nThank you for shopping with us!")
        OrderHistory().log_order_history(self.cart, username)
        logging.info(f"Checkout complete. Total bill: ${total_bill}")

class OrderHistory:
    def __init__(self):
        self.base_folder = "USER_HISTORY"
        pass

    def log_order_history(self, cart, username):
        logging.info(f"Logging order history for user {username}")
        user_history_file = f"{self.base_folder}/{username}_history.txt"
        current_time = time.strftime("%H:%M:%S")
        current_date = datetime.date.today().strftime("%Y-%m-%d")
        with open(user_history_file, 'a') as f:
            f.write(f"Order Date: {current_date} Time: {current_time}\n")
            for cart_item in cart:
                f.write(f"{cart_item['quantity']} {cart_item['item'].name} - ${cart_item['item'].price} each\n")
            f.write("\n")
        logging.info(f"Order history logged for user {username}")

    def view_order_history(self, username):
        logging.info(f"Viewing order history for user {username}")
        user_history_file = f"{self.base_folder}/{username}_history.txt"
        try:
            with open(user_history_file, 'r') as f:
                print('Your order history:')
                logging.info(f"Order history displayed for user {username}")
                for line in f:
                    print(line.strip())
        except FileNotFoundError:
            print("No order history found.")
            logging.warning(f"No order history found for user {username}")

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, total_amount):
        pass

class Payment(PaymentProcessor):
    def process_payment(self, total_amount):
        print(f"Processing payment of ${total_amount}")

class AmoStore:
    def __init__(self):
        self.menu = Menu()
        self.shopping_cart = UserShoppingCart()
        self.order_history_manager = OrderHistory()
        self.payment_gateway = Payment()




    def authenticate_user(self, username, password):
        try:
            with open('user_information.txt', 'r') as f:
                for line in f:
                    parts = line.strip().split(':')
                    if len(parts) != 2:
                        print(f"Skipping improperly formatted line: {line.strip()}")
                        continue
                    stored_username, stored_password = parts
                    if stored_username == username and stored_password == password:
                        return True
            return False
        except FileNotFoundError:
            return False

    def signup(self):
     logging.info("Signup process started")
     while True:
        first_name = input("Enter your first name: ").strip()
        last_name = input("Enter your last name: ").strip()
        
        # Validate first name and last name length and no spaces
        if len(first_name) < 3 or len(last_name) < 3 or ' ' in first_name or ' ' in last_name:
            print("First name and last name must be at least 3 characters long and should not contain spaces.")
            continue
        
        while True:
            username = input("Enter your username: ").strip()
            if len(username) < 4 or ' ' in username:
                print("Username must be at least 4 characters long and should not contain spaces.")
            elif self.user_exists(username):
                print("Username already taken. Please choose another username.")
            else:
                break
        print("Password must be at least 8 characters long and contain at least one uppercase letter, one digit, and one special character.")
        while True:
            password = input("Enter your password: ").strip()
            
            # Validate password criteria
            has_upper = any(c.isupper() for c in password)
            has_digit = any(c.isdigit() for c in password)
            has_special = any(not c.isalnum() for c in password)
            
            if len(password) < 8 or not (has_upper and has_digit and has_special):
                print("Password must be at least 8 characters long and contain at least one uppercase letter, one digit, and one special character.")
            else:
                break
        
        # If all checks pass, proceed with signup
        with open('user_information.txt', 'a') as f:
            f.write(f"{username}:{password}\n")
        
        print("Signup successful!")
        logging.info(f"New user signed up: {username}")
        break


    def login(self):
        logging.info("Login process started")
        while True:
            username = input("Enter your username::(ENTER ### AND LEAVE PASSWORD BLANK FOR RETURN TO MAIN MENU): ")
            password = input("Enter your password: ")
            if username == "###":
                return None 
            if self.authenticate_user(username, password):
                print(f"Welcome, {username}!")
                return username
            else:
                print("Invalid username or password. Please try again.")
                logging.warning("Login failed")
    def user_exists(self, username):
        try:
            with open('user_information.txt', 'r') as f:
                for line in f:
                    if line.split(':')[0] == username:
                        return True
            return False
        except FileNotFoundError:
            return False

    def start_shopping(self, username):
        while True:
            self.menu.display_menu()
            choice = input("\n1. Add item to cart\n2. Remove item from cart\n3. View cart\n4. Checkout\n5. View order history\n6. Logout\nEnter your choice: ")

            if choice == '1':
                while True:
                    item_no_str = input("Enter the item number you want to add to the cart: ")
                    if not item_no_str.isdigit():  # Check if input is a number
                        print("Invalid input. Please enter a valid item number.")
                        continue

                    item_no = int(item_no_str)
                    if item_no in self.menu.items:
                        break  # Valid item number, break the inner loop
                    else:
                        print("Invalid item number.")
                
                while True:
                    quantity_str = input(f"Enter the quantity of {self.menu.items[item_no].name}: ")
                    if not quantity_str.isdigit():  # Check if input is a number
                        print("Invalid input. Please enter a valid quantity.")
                        continue

                    quantity = int(quantity_str)
                    self.shopping_cart.add_to_cart(self.menu.items[item_no], quantity)
                    break
            elif choice == '2':
                self.shopping_cart.view_cart()
                item_name = input("Enter the name of the item you want to remove from the cart: ")
                self.shopping_cart.remove_from_cart(item_name)
            elif choice == '3':
                self.shopping_cart.view_cart()
            elif choice == '4':
                total_amount = sum(item['item'].price * item['quantity'] for item in self.shopping_cart.cart)
                self.payment_gateway.process_payment(total_amount)
                self.shopping_cart.checkout(username)
                self.shopping_cart.cart.clear()
            elif choice == '5':
                self.order_history_manager.view_order_history(username)
            elif choice == '6':
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")
                logging.warning("Invalid menu choice entered.")


def print_centered(text, width):
    """Prints text centered within a box of specified width."""
    padding = (width - len(text)) // 2
    print(f"{'-' * width}")
    print(f"|{' ' * padding}{text}{' ' * padding}|")
    print(f"{'-' * width}")

def main():
    amo_store = AmoStore()
    while True:
        print_centered("Welcome to AmoStore", 70)
        print_centered("1. Signup", 70)
        print_centered("2. Login", 70)
        print_centered("3. Exit", 70)
        choice = input("Enter your choice: ")
        if choice == '1':
            amo_store.signup()
        elif choice == '2':
            username = amo_store.login()
            if username is None:
                continue  # Go back to main menu display
            if username:
                amo_store.start_shopping(username)
        elif choice == '3':
            print_centered("Thank you for visiting AmoStore!", 70)
            logging.info("Program exited")
            break
        else:
            print_centered("Invalid choice. Please try again.", 70)
            logging.warning("Invalid main menu choice entered.")

if __name__ == "__main__":
    main()

