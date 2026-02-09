
# 💊 Pharmacy Management System

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A **simple Pharmacy Management System** written in Python.
This program allows you to:

* 💾 Add new medicines
* 📦 View inventory
* 🛒 Sell medicine
* 🔍 Search for a medicine

---

## 🚀 How to Run

1. Make sure **Python 3.7 or higher** is installed on your computer.
2. Open a terminal or command prompt and navigate to the project folder.
3. Run the program by typing:
   python pharmacy_management.py

---

## 🧪 How to Test

The program includes a **test section** at the bottom (`if __name__ == "__main__":`) that demonstrates how the system works.

The test performs the following actions:

* Adds medicines: Paracetamol, Ibuprofen, Amoxicillin
* Shows the current inventory
* Sells medicines (checks if stock is enough)
* Searches for medicines (both existing and missing)
* Shows inventory after sales

**Expected output example:**

Medicine 'Paracetamol' added to inventory.
Medicine 'Ibuprofen' added to inventory.
Medicine 'Amoxicillin' added to inventory.

--- Inventory ---
Paracetamol - $1.5 - Qty: 50
Ibuprofen - $2.0 - Qty: 30
Amoxicillin - $3.0 - Qty: 20

--- Sell Medicine ---
Sold 10 units of 'Paracetamol'.
Not enough stock for 'Ibuprofen'. Available: 30

--- Search Medicine ---
Medicine Found:
Amoxicillin - $3.0 - Qty: 20
Medicine 'Aspirin' not found.

--- Inventory After Sales ---
Paracetamol - $1.5 - Qty: 40
Ibuprofen - $2.0 - Qty: 30
Amoxicillin - $3.0 - Qty: 20

---

## 💡 Lessons Learned (OOP Concepts)

From building this project, I learned:

1. **Classes & Objects**

   * `Medicine` class represents each medicine
   * `Pharmacy` class manages the inventory

2. **Encapsulation**

   * Medicine properties (`name`, `price`, `quantity`) are stored inside the `Medicine` class

3. **Methods**

   * Functions like `add_medicine()`, `sell_medicine()`, and `search_medicine()` organize program behavior

4. **Code Reusability & Organization**

   * Separate methods for adding, selling, and searching make the code clean and easy to manage

5. **Real-world Modeling**

   * OOP allows us to model a real pharmacy system in a program

---

## 📄 License

This project is licensed under the **MIT License**.


