
# ☕ Coffee Machine Simulator

A simple Python-based Coffee Machine Simulator that mimics the behavior of a real coffee vending machine. Users can order different types of coffee, insert virtual coins, receive change, and view machine resource reports.

## 🚀 Features

* Order coffee:

  * Espresso
  * Latte
  * Cappuccino
* Coin-based payment system
* Automatic change calculation
* Resource management system
* Machine report generation
* Continuous ordering loop
* Refund system for insufficient resources or payment

---

## 📋 Coffee Menu

| Coffee Type | Price |
| ----------- | ----- |
| Espresso    | $3.00 |
| Latte       | $4.50 |
| Cappuccino  | $6.00 |

---

## 💰 Supported Coins

| Coin    | Value |
| ------- | ----- |
| Penny   | $0.01 |
| Nickel  | $0.05 |
| Dime    | $0.10 |
| Quarter | $0.25 |

---

## 🛠 Initial Resources

| Resource | Quantity |
| -------- | -------- |
| Milk     | 750 mL   |
| Coffee   | 200 g    |
| Water    | 800 mL   |

---

## 📦 Requirements

* Python 3.x

No external libraries are required.

---

## ▶️ How to Run

1. Clone this repository

```bash
git clone https://github.com/your-username/coffee-machine-simulator.git
```

2. Navigate to the project folder

```bash
cd coffee-machine-simulator
```

3. Run the program

```bash
python main.py
```

---

## 📸 Example Usage

```text
What would you like to have (espresso/latte/cappuccino) latte

How much penny you are inserting 0
How much nickel you are inserting 0
How much dimes you are inserting 10
How much quarter you are inserting 15

Your latte is ready...Enjoy your day
The exchange of $0.25 has been returned successfully
```

---

## 📊 Report Command

Type:

```text
report
```

to view the current machine resources and total earnings.

Example:

```text
Total milk we have = 650
Total coffee we have = 130
Total Water we have = 670
Total money we have is 4.5
```

---

## 🎯 Learning Objectives

This project helped practice:

* Python Functions
* Conditional Statements
* Loops
* User Input Handling
* Global Variables
* Basic Resource Management
* Simple Business Logic Implementation

---

## 🔮 Future Improvements

* Store resources in dictionaries
* Add machine refill functionality
* Save earnings to a file
* Create a graphical user interface (GUI)
* Add inventory alerts
* Improve code structure using OOP

---

## 👨‍💻 Author

Prem Kumar

Built as a Python practice project to strengthen programming fundamentals and problem-solving skills.
