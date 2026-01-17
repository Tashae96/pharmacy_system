# pharmacy_management.py

class Medicine:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ${self.price} - Qty: {self.quantity}"


class Pharmacy:
    def __init__(self):
        self.inventory = []

    def add_medicine(self, name, price, quantity):
        # Check if medicine already exists
        for med in self.inventory:
            if med.name.lower() == name.lower():
                med.quantity += quantity
                print(f"{quantity} units added to existing medicine '{name}'.")
                return
        # Add new medicine
        self.inventory.append(Medicine(name, price, quantity))
        print(f"Medicine '{name}' added to inventory.")

    def view_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
            return
        print("Current Inventory:")
        for med in self.inventory:
            print(med)

    def sell_medicine(self, name, quantity):
        for med in self.inventory:
            if med.name.lower() == name.lower():
                if med.quantity >= quantity:
                    med.quantity -= quantity
                    print(f"Sold {quantity} units of '{name}'.")
                    return
                else:
                    print(f"Not enough stock for '{name}'. Available: {med.quantity}")
                    return
        print(f"Medicine '{name}' not found in inventory.")

    def search_medicine(self, name):
        for med in self.inventory:
            if med.name.lower() == name.lower():
                print("Medicine Found:")
                print(med)
                return
        print(f"Medicine '{name}' not found.")


# Testing the Pharmacy Management System
if __name__ == "__main__":
    pharmacy = Pharmacy()

    # Add medicines
    pharmacy.add_medicine("Paracetamol", 1.5, 50)
    pharmacy.add_medicine("Ibuprofen", 2.0, 30)
    pharmacy.add_medicine("Amoxicillin", 3.0, 20)

    print("\n--- Inventory ---")
    pharmacy.view_inventory()

    print("\n--- Sell Medicine ---")
    pharmacy.sell_medicine("Paracetamol", 10)
    pharmacy.sell_medicine("Ibuprofen", 40)  # Not enough stock

    print("\n--- Search Medicine ---")
    pharmacy.search_medicine("Amoxicillin")
    pharmacy.search_medicine("Aspirin")  # Not found

    print("\n--- Inventory After Sales ---")
    pharmacy.view_inventory()
