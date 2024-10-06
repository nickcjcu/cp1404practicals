number_of_items = int(input("Number of items: "))
total_price = 0
for item in range(number_of_items):
    amount = float(input("Price of item: "))
    total_price = total_price + amount
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
