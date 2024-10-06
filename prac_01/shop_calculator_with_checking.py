total_price = 0
number_of_items = 0

number_of_items = int(input("Number of items (or a negative number to exit): "))

while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items (or a negative number to exit): "))

total_price_for_items = 0

for item in range(number_of_items):
    amount = float(input("Price of item: "))
    total_price_for_items += amount

total_price += total_price_for_items
print(f"Total price for {number_of_items} items is ${total_price_for_items:.2f}")
print(f"Final total price is ${total_price:.2f}")
