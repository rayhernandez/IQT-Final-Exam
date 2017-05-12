import math
import inspect


def circle():
    """
    This function will take in radius from user input and
    print the Diameter, Circumference, and Area of a Circle
    """
    print(inspect.getdoc(circle))
    while True:
        radius = float(input("\nEnter the Radius Value: "))
        diameter = (radius*2)
        circumference = (math.pi*diameter)
        area = (math.pi*(radius ** 2))

        print("\nDiameter: ", diameter)
        print("Circumference: ", circumference)
        print("Area: ", area)

print(circle())
