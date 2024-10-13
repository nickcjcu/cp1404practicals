"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?

    when you use for example letters instead of numbers

2. When will a ZeroDivisionError occur?

    when you try to make the denominator 0

3. Could you change the code to avoid the possibility of a ZeroDivisionError?

    I couldn't so I went onto the making change step in exception complete file

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
