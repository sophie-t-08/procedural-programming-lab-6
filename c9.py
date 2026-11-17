numbers = [10, 20, 30, 40]
index = int(input("Enter an index number: "))
divisor = int(input("Enter a divisor: "))
result = numbers[index] / divisor
print("Result:", result)

#error 1: value error
#error 2: index error
#error 3: zero division error

try:
    numbers = [10, 20, 30, 40]
    index = int(input("Enter an index number: "))
    divisor = int(input("Enter a divisor: "))
    result = numbers[index] / divisor
    print("Result:", result)
except ValueError:
    print("Invalid input, please enter integers only")
except IndexError:
    ("Out of list index range, please enter a number in range")
except ZeroDivisionError:
    print("Cannot divide by zero, please enter a larger integer")