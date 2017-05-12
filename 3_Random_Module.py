import random
import inspect


def add():
    """
    This function will randomly set x and y to a number between 1 and 9,
    then ask the user to input the sum of the two numbers.
    """
    print(inspect.getdoc(add))
    while True:
        x = random.randint(1, 9)
        y = random.randint(1, 9)
        print("\nx =", x)
        print("y =", y)
        print("\nWhat is the sum of x and y?")
        userinput = int(input("Enter the Sum of x and y:  "))
        if userinput == (x+y):
            print("\nYour answer is CORRECT!")

        elif userinput != (x+y):
            print("\nYour answer is INCORRECT.")
print(add())
