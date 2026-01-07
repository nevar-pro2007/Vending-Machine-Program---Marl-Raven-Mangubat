# Vending Machine Program

class VendingMachine:
    def __init__(self):
        # Items that are available in the machine with categories
        self.snacks = {
            31: {"name": "Pringles Cheese", "price": 10.00, "stock": 10, "pair": 37},
            32: {"name": "Ritz Crackers", "price": 11.00, "stock": 10, "pair": 40},
            33: {"name": "Twix Rolls", "price": 8.00, "stock": 10, "pair": 39},
            34: {"name": "Bugles Natcho", "price": 7.00, "stock": 10, "pair": 36},
            35: {"name": "Oreo Biscuit", "price": 5.00, "stock": 10, "pair": 39},
        }
        self.drinks = {
            36: {"name": "Sprite", "price": 3.00, "stock": 10, "pair": 34},
            37: {"name": "Coca-Cola", "price": 3.00, "stock": 10, "pair": 31},
            38: {"name": "Berain Water", "price": 1.00, "stock": 10, "pair": 32},
            39: {"name": "Saudia Choco Milk", "price": 2.50, "stock": 10, "pair": 33},
            40: {"name": "Almarai Apple Juice", "price": 4.50, "stock": 10, "pair": 35},
        }
        self.categories = {
            "Snacks": self.snacks,
            "Drinks": self.drinks,
        }
        self.run()

    # Displays the welcome message
    def display_welcome_message(self):
        """Displays the welcome message."""
        print("\n" + "=" * 35)
        print("WELCOME TO NEVAR VENDING MACHINE!")
        print("\n" + "=" * 35)

    # Displays the main menu and handles user selection
    def main_menu(self):
        """Displays the main menu and handles user selection."""
        while True:
            print("\nMAIN MENU: ")
            print("1. Snacks")
            print("2. Drinks")
            print("3. Exit")
            choice = input("Select an option (1-3): ")

            if choice in ["1", "2"]:
                # Determining which category to show
                category_key = list(self.categories.keys())[int(choice) - 1]
                self.category_menu(category_key, self.categories[category_key])
            elif choice == "3":
                print("Thank you for using Nevar Vending Machine! Goodbye!")
                break
            else:
                print("Invalid option! Please enter 1-3.")

    # Presents specific items and captures user codes        
    def category_menu(self, name, items):
        """Presents specific items and captures user codes."""
        print(f"\n--- {name.upper()} MENU ---")
        for code, details in items.items():
            stock_status = f"Stock: {details['stock']}" if details['stock'] > 0 else "Stock Unavailable!"
            print(f"[{code}] {details['name']} - ${details['price']:.2f} ({stock_status})")

        selected_items = {}
        while True:
            item_code = input("\nEnter code to select (or 0 to finish order): ")
            if item_code == "0":
                break
            
            # Capturing inputted code
            if item_code.isdigit() and int(item_code) in items:
                code = int(item_code)
                if items[code]["stock"] <= 0:
                    print(f"Sorry, {items[code]['name']} is out of stock.")
                    continue
                
                # Buying multiple items
                qty_input = input(f"How many {items[code]['name']}? ")
                if qty_input.isdigit() and int(qty_input) > 0:
                    qty = int(qty_input)
                    if qty <= items[code]["stock"]:
                        selected_items[code] = selected_items.get(code, 0) + qty
                        print(f"Added {qty} x {items[code]['name']} to cart.")
                    else:
                        print(f"Insufficient stock. Only {items[code]['stock']} available.")
                else:
                    print("Invalid quantity.")
            else:
                print("Invalid code. Please try again.")

        if selected_items:
            self.process_payment(items, selected_items)

    # Manages money, returns change, and dispenses items
    # This section is generated with the help of Google Gemini 3 (2025)
    # Prompt: Generate me a code for payment process
    # Modification: Added dispensing items and returning change
    def process_payment(self, items, selected_items):
        """Manages money, returns change, and dispenses items."""
        total_cost = sum(items[code]["price"] * qty for code, qty in selected_items.items())
        print(f"\nTOTAL DUE: ${total_cost:.2f}")

        while True:
            payment_input = input("Insert money (or type 'cancel'): $")
            if payment_input.lower() == 'cancel':
                print("Transaction cancelled. Returning to menu.")
                return

            try:
                payment = float(payment_input)
                if payment >= total_cost:
                    # Dispensing and change management
                    change = payment - total_cost
                    print("\n--- DISPENSING ITEMS ---")
                    for code, qty in selected_items.items():
                        print(f"Dispensed: {qty} x {items[code]['name']}")
                        items[code]["stock"] -= qty
                    
                    print(f"Change Returned: ${change:.2f}")
                    self.suggest_items(selected_items)
                    break
                else:
                    print(f"Insufficient balance. You still owe ${total_cost - payment:.2f}")
            except ValueError:
                print("Invalid input. Please enter an amount.")

    # Function for intelligence system and purchase suggestion based on user selection
    def suggest_items(self, last_purchase):
        """Intelligence system for suggesting purchases based on selection."""
        print("\n--- SMART SUGGESTION ---")
        for code in last_purchase:
            # Checks for paired items in snacks or drinks dictionaries
            pair_code = None
            if code in self.snacks:
                pair_code = self.snacks[code]["pair"]
                suggestion = self.drinks.get(pair_code)
            elif code in self.drinks:
                pair_code = self.drinks[code]["pair"]
                suggestion = self.snacks.get(pair_code)
            
            if suggestion and suggestion['stock'] > 0:
                print(f"Enjoy your purchase! Why not try {suggestion['name']} next time?")
                break # Suggest only one item

    def run(self):
        """Starts the machine."""
        self.display_welcome_message()
        self.main_menu()

# Run the vending machine program
if __name__ == "__main__":
    VendingMachine()
