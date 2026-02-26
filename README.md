# 💰 Personal Budget Tracker (Command-Line Utility)

## 📌 Project Overview

The **Personal Budget Tracker** is a command-line financial management tool developed using the **Python programming language**.  

The purpose of this application is to help users — especially first-year university students — monitor their spending against a predetermined budget over a given period (such as a week).

The system tracks financial transactions, continuously calculates total expenses, provides real-time warnings if the budget is exceeded, and generates a comprehensive financial summary at the end of the session.

This project demonstrates how Python can be used to solve real-life problems such as personal money management.

---

## 🎯 Project Objectives

The main objectives of this project are:

- To help users manage personal finances responsibly
- To apply fundamental Python programming concepts
- To practice user input handling and data validation
- To demonstrate real-time budget monitoring
- To generate structured financial reports

---

## ⚙️ How the Application Works

### 1️⃣ Budget Initialization

When the program starts, the user is required to enter a **budget amount**.

- The budget must be a **non-negative number**
- This represents the maximum amount the user plans to spend
- The budget remains fixed throughout the session
- All expenses entered later are compared against this value

---

### 2️⃣ Transaction Logging

The program allows the user to enter multiple financial transactions.

Each transaction includes:

- 📝 A **textual description**  
  Example:  
  - `Lunch at Bobics`  
  - `Transport to Bugujju`

- 💵 A **numerical amount**

For testing purposes, the system supports **at least five transactions**, though the user may enter more depending on the implementation.

All transactions are stored and later displayed in the final summary.

---

### 3️⃣ Real-Time Expense Monitoring

After each transaction is entered:

- The system updates the **cumulative total of expenses**
- It immediately checks whether the total exceeds the initial budget

If the budget is exceeded:

- ⚠️ A clear warning message is displayed
- The user is notified instantly about overspending

This feature promotes financial awareness and responsible spending.

---

### 4️⃣ Ending the Input Session

The user signals the end of the transaction entry session (for example, by typing `done` or `exit`, depending on implementation).

Once the session ends:

- No additional transactions are accepted
- The program proceeds to generate the final report

---

### 5️⃣ Final Financial Summary

At the end of the session, the application generates a detailed summary report containing:

- 📊 Initial budget
- 💰 Total recorded expenses
- ✅ Remaining balance (if within budget)  
  **OR**
- ❌ Deficit amount (if budget was exceeded)

The summary also includes a **detailed transaction log** listing:

- Each expense description
- The corresponding amount spent

This provides a complete overview of the user's financial activity.

---

## 🧠 Programming Concepts Applied

This project demonstrates the use of:

- Variables and data types
- User input handling (`input()`)
- Conditional statements (`if`, `else`)
- Loops (`while` or `for`)
- Lists for storing transactions
- Basic arithmetic operations
- Output formatting

---

## 🖥️ Example Usage

```bash
Enter your weekly budget: 100000

Enter expense description: Lunch at Bobics
Enter amount: 15000

Enter expense description: Transport to Bugujju
Enter amount: 10000
