name = input("What's your name? ")
file = open('name.txt', 'w')
file.write(name)
file.close()

file = open('name.txt', 'r')
name_from_file = file.read().strip()
file.close()
print(f"Hi {name_from_file}!")

with open('numbers.txt', 'r') as file:
    number1 = int(file.readline().strip())
    number2 = int(file.readline().strip())
    print(number1, number2)
    result = number1 + number2
print(result)


total = 0
with open('numbers.txt', 'r') as file:
    for line in file:
        total += int(line.strip())
print(total)
