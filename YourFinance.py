import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class FinanceTracker:
    def __init__(self, master):
        self.master = master
        self.master.title("Personal Finance Tracker")

        # Initialize budget and expenses
        self.budget = {'Food': 0, 'Rent': 0, 'Travel': 0, 'Phone Bills': 0, 'Other': 0}
        self.income = 0
        self.expenses = {'Food': 0, 'Rent': 0, 'Travel': 0, 'Phone Bills': 0, 'Other': 0}

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Set Budget").grid(row=0, column=0, columnspan=2)
        self.create_budget_entries()

        tk.Label(self.master, text="Income").grid(row=6, column=0)
        self.income_entry = tk.Entry(self.master)
        self.income_entry.grid(row=6, column=1)
        tk.Button(self.master, text="Add Income", command=self.add_income).grid(row=7, columnspan=2)

        tk.Label(self.master, text="Expense").grid(row=8, column=0)
        self.expense_entry = tk.Entry(self.master)
        self.expense_entry.grid(row=8, column=1)
        self.category_var = tk.StringVar(value='Food')
        tk.OptionMenu(self.master, self.category_var, *self.budget.keys()).grid(row=9, column=1)
        tk.Button(self.master, text="Add Expense", command=self.add_expense).grid(row=10, columnspan=2)

        tk.Button(self.master, text="Show Summary", command=self.show_summary).grid(row=11, columnspan=2)

    def create_budget_entries(self):
        for i, category in enumerate(self.budget.keys()):
            tk.Label(self.master, text=category).grid(row=i+1, column=0)
            entry = tk.Entry(self.master)
            entry.grid(row=i+1, column=1)
            self.budget[category] = entry

    def add_income(self):
        try:
            income = float(self.income_entry.get())
            self.income += income
            messagebox.showinfo("Info", f"Income added: {income}")
            self.income_entry.delete(0, tk.END)  # Clear entry
        except ValueError:
            messagebox.showerror("Error", "Invalid income value.")

    def add_expense(self):
        category = self.category_var.get()
        try:
            expense = float(self.expense_entry.get())
            self.expenses[category] += expense
            messagebox.showinfo("Info", f"Expense added: {expense} to {category}")
            self.expense_entry.delete(0, tk.END)  # Clear entry
        except ValueError:
            messagebox.showerror("Error", "Invalid expense value.")

    def show_summary(self):
        total_expenses = sum(self.expenses.values())
        budget_status = "\n".join([f"{cat}: Budget {self.budget[cat].get()} - Spent {self.expenses[cat]} = Remaining {float(self.budget[cat].get()) - self.expenses[cat]}" for cat in self.budget])
        messagebox.showinfo("Summary", f"Total Income: {self.income}\nTotal Expenses: {total_expenses}\nBudget Status:\n{budget_status}")
        self.plot_expenses()

    def plot_expenses(self):
        categories = list(self.expenses.keys())
        values = list(self.expenses.values())
        plt.pie(values, labels=categories, autopct='%1.1f%%')
        plt.title('Expenses by Category')
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceTracker(root)
    root.mainloop()
