"""
Personal Finance Manager
A simple command-line budget tracking system.
"""

from dataclasses import dataclass
from typing import List


#  Constants

MIN_TRANSACTIONS = 5
EXIT_COMMAND = "done"


# -------------------- Data Model

@dataclass
class Transaction:
    """Represents a single financial transaction."""
    #Single Responsibility principle
    description: str
    amount: float


# -------------------- Core Logic --------------------

class BudgetManager:
    """Handles budget tracking and transaction management."""

    def __init__(self, budget: float) -> None:
        self._validate_budget(budget)
        self.budget = budget

        # -------an aspect of composition-------
        self.transactions: List[Transaction] = []

    def _validate_budget(self, budget: float) -> None:
      #--------an aspect of invariance------
        if budget < 0:
          raise ValueError("Budget cannot be negative.")

    def add_transaction(self, transaction: Transaction) -> None:
        self.transactions.append(transaction)

    def total_spent(self) -> float:
        return sum(t.amount for t in self.transactions)

    def remaining_balance(self) -> float:
        return self.budget - self.total_spent()

    def is_budget_exceeded(self) -> bool:
        return self.total_spent() > self.budget


# -------------------- Input Handling --------------------

def get_valid_float(prompt: str) -> float:
    """Safely get a valid non-negative float from user."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Amount must not be negative.")
                continue
            return value
        except ValueError:
            print("Invalid number. Please enter a valid amount.")


def get_transaction_input() -> Transaction:
    """Collect transaction details from user."""
    description = input("Enter description: ").strip()
    amount = get_valid_float("Enter amount: ")
    return Transaction(description, amount)


# -------------------- Reporting --------------------

def print_summary(manager: BudgetManager) -> None:
    """Display final financial report."""
    print("\n========== FINAL SUMMARY ==========")
    print(f"Initial Budget: {manager.budget:.2f}")
    print(f"Total Expenses: {manager.total_spent():.2f}")

    balance = manager.remaining_balance()

    if balance >= 0:
        print(f"Remaining Balance: {balance:.2f}")
    else:
        print(f"Deficit: {abs(balance):.2f}")

    print("\nTransactions:")
    for index, transaction in enumerate(manager.transactions, start=1):
        print(f"{index}. {transaction.description} - {transaction.amount:.2f}")

    print("===================================")


# -------------------- Main Program --------------------

def main() -> None:
    print("Welcome to Personal Finance Manager\n")

    budget = get_valid_float("Enter your budget: ")
    manager = BudgetManager(budget)

    print(f"\nEnter at least {MIN_TRANSACTIONS} transactions.")
    print(f"Type '{EXIT_COMMAND}' as description when finished.\n")

    transaction_count = 0

    while True:
        description = input("Enter description: ").strip()

        if description.lower() == EXIT_COMMAND:
            if transaction_count < MIN_TRANSACTIONS:
                print(f"You must enter at least {MIN_TRANSACTIONS} transactions.")
                continue
            break

        amount = get_valid_float("Enter amount: ")
        transaction = Transaction(description, amount)
        manager.add_transaction(transaction)

        transaction_count += 1

        if manager.is_budget_exceeded():
            print("WARNING: Budget exceeded!")

        print(f"Current Total Spent: {manager.total_spent():.2f}\n")

    print_summary(manager)


if __name__ == "__main__":
    main()