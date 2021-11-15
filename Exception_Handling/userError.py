class GuessError(Exception):
    def __init__(self, message):
        self.message = message

a = int(input("Enter the input : "))
		
try:
    if a < 3:
        raise GuessError("Your guess is wrong. Number is less.")
    elif a > 3:
        raise GuessError("Your guess is wrong. Number is high.")
    else:
        print("Your guess is right. The value is : {}.".format(a))
except GuessError as e:
    print(e.message)
