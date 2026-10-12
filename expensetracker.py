expenses = []

while True:
    item = input("Enter expense name (or type 'done'): ")

    if item.lower() == "done":
        break

    amount = float(input("Enter amount: "))
    expenses.append((item, amount))

total = 0

for item, amount in expenses:
    total += amount

print("\nYour expenses:")

for item, amount in expenses:
    print(item, "₹", amount)

print("\nTotal spending: ₹", total)