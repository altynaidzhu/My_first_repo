try:
    number = int(input("Enter a number:"))
    result = 10/number
except ZeroDivisionError:
    print("Error: Division by zero!")
finally:
    print("This will always print.")