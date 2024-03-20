'''Expense Tracker: Develop a program that helps users track their daily expenses. 
Users should be able to add expenses, categorize them, and view summaries.'''

import streamlit as st

# Defining Function to add expense
def add_expense(expenses):
    amount = st.number_input("Enter amount:", step=0.01, format="%.2f")
    category = st.text_input("Enter category:")
    if st.button("Add Expense"):
        expenses.append({"Amount": amount, "Category": category})
        st.success("Expense added successfully!")

# Defining Function to view expenses
def view_expenses(expenses):
    if not expenses:
        st.info("No expenses recorded yet.")
    else:
        st.write("Expense Summary:")
        for idx, expense in enumerate(expenses, start=1):
            st.write(f"{idx}. Amount: ${expense['Amount']}, Category: {expense['Category']}")

# Defining Function to view summary by category
def summary_by_category(expenses):
    category_summary = {}
    for expense in expenses:
        category = expense["Category"]
        if category not in category_summary:
            category_summary[category] = 0
        category_summary[category] += expense["Amount"]

    if not category_summary:
        st.info("No expenses recorded yet.")
    else:
        st.write("Summary by Category:")
        for category, total_amount in category_summary.items():
            st.write(f"{category}: ${total_amount}")

# Defining Main function
def main():
    st.title("Expense Tracker")

    # Initialize list to store expenses
    if "expenses" not in st.session_state:
        st.session_state.expenses = []

    # Sidebar options
    st.sidebar.title("Menu")
    menu_choice = st.sidebar.radio("Select:", ["Add Expense", "View Expenses", "Summary by Category"])

    # Perform actions based on menu choice
    if menu_choice == "Add Expense":
        add_expense(st.session_state.expenses)
    elif menu_choice == "View Expenses":
        view_expenses(st.session_state.expenses)
    elif menu_choice == "Summary by Category":
        summary_by_category(st.session_state.expenses)

if __name__ == "__main__":
    main()
