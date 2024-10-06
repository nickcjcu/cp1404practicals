"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
final_amount = 0
sales = 0
while sales >= 0:
    sales = float(input("Enter sales: $"))
    if sales >= 1000:
        final_amount = sales + (sales * 0.15)
        print(f"${final_amount}")
    elif sales >= 0 and sales < 1000:
        final_amount = sales + (sales * 0.1)
        print(f"${final_amount}")
    else:
        exit()
