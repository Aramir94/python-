a = 2
b = 5 
try:
    print("Program is running")
    print(a/b)
    print("program has worked")
    i = int(input("Enter input : "))

except ZeroDivisionError:
    print("Error: Division by zero is not possible")

except Exception:
    print("Invalid Input")

finally:
	print("program has successfully ended...")
'''
when input is string Invaild Input error
when b = 0 Division by zero is not possible
'''
