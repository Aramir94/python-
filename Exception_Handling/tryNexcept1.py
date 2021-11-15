a = 2
b = 0
try:
    print("Program is running")
    print(a/c)
    print("program has worked")
except ZeroDivisionError as e:
    print("Error: Division by zero is not")
except SyntaxError as e:
    print("Error : Check your syntax")
except NameError as e:
    print("Error : Variable not found")
finally:
    print("Program has successfully ended")

