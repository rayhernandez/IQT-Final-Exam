import math
import inspect


def pythagorean_equation():
    """
    This function will automatically print out all possible
    hypotenuse values of a triangle with sides no greater than 20.
    """
    print(inspect.getdoc(pythagorean_equation))
    for i in range(0, 21, 1):
        SideA = i
        print(SideA)
        for j in range(0, 21, 1):
            SideB = j
            # print(SideB)
            # print(SideA, "&", SideB)
            SideC = math.sqrt((SideA**2)+(SideB**2))
            print("\nSideA:", SideA, "\nSideB:", SideB, "\nThe Hypotenuse is:",  round(SideC, 2))

print(pythagorean_equation())
