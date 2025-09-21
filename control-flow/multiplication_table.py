# multiplication_table.py

# Prompt user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print multiplication table from 1 to 10
for i in range(1, 10 + 1):
    product = number * i
    print(f"{number} * {i} = {product}")
# multiplication_table.py

# Prompt User for a Number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and Print the Multiplication Table from 1 to 10
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")
