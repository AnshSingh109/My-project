
import csv
import matplotlib.pyplot as plt

# File to store expense data
FILE_NAME = "expenses.csv"

# Initialize the file with headers if it doesn't exist
def initialize_file():
    try:
        with open(FILE_NAME, 'x') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount"])
    except FileExistsError:
        pass

# Add an expense
def add_expense(date, category, amount):
    with open(FILE_NAME, 'a') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
    print("Expense added successfully!")

# View all expenses
def view_expenses():
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Generate a summary
def generate_summary():
    expenses = {}
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            category = row[1]
            amount = float(row[2])
            expenses[category] = expenses.get(category, 0) + amount
    for category, total in expenses.items():
        print(f"{category}: ${total:.2f}")
    return expenses

# Visualize data
def visualize_data():
    data = generate_summary()
    categories = data.keys()
    amounts = data.values()
    
    plt.figure(figsize=(8, 5))
    plt.bar(categories, amounts, color='skyblue')
    plt.title("Expense Breakdown")
    plt.xlabel("Category")
    plt.ylabel("Amount Spent")
    plt.show()

# Main menu
def main():
    initialize_file()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Generate Summary")
        print("4. Visualize Data")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category (e.g., Food, Transport): ")
            amount = input("Enter amount: ")
            add_expense(date, category, float(amount))
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            generate_summary()
        elif choice == "4":
            visualize_data()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
