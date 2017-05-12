# http://cs.colgate.edu/~jsommers/cosc101/html/oo.html#a-rectangle-class
# CLASS Reference: https://www.codesdope.com/python-your-class
# Point/Ordered Pair Reference: https://www.cs.uky.edu/~keen/115/Haltermanpythonbook.pdf

import inspect


class Rectangle:
    def __init__(self, i_length, i_width, t_top_left, t_bottom_right):
        self.i_length = i_length
        self.i_width = i_width
        self.t_top_left = t_top_left
        self.t_bottom_right = t_bottom_right

    def perimeter_input(self):
        """
        This function will calculate the perimeter of a rectangle using length and width.
        """
        print(inspect.getdoc(Rectangle.perimeter_input()))
        return 2*(self.i_length+self.i_width)

    def area_input(self):
        """
        This function will calculate the area of a rectangle using length and width.
        """
        print(inspect.getdoc(Rectangle.area_input()))
        return self.i_length*self.i_width

    def length_tuple(self):
        """
        This function will calculate the length of a rectangle using top-left and bottom-right corners of the rectangle.
        """
        print(inspect.getdoc(Rectangle.length_tuple()))
        return abs((self.t_top_left[0])-(self.t_bottom_right[0]))

    def width_tuple(self):
        """
        This function will calculate the width of a rectangle using top-left and bottom-right corners of the rectangle.
        """
        print(inspect.getdoc(Rectangle.width_tuple()))
        return (self.t_top_left[1])-(self.t_bottom_right[1])

    def perimeter_tuple(self):
        """
        This function will calculate the perimeter of a rectangle using top-left and bottom-right corners of the rectangle.
        """
        return (2*(abs(self.t_top_left[0])+abs(self.t_bottom_right[0]))+(2*(abs(self.t_top_left[1])+abs(self.t_bottom_right[1]))))

    def area_tuple(self):
        """
        This function will calculate the area of a rectangle using top-left and bottom-right corners of the rectangle.
        """
        print(inspect.getdoc(Rectangle.area_tuple()))
        return ((abs(self.t_top_left[0])+abs(self.t_bottom_right[0]))*((abs(self.t_top_left[1])+abs(self.t_bottom_right[1]))))

    def square(self):
        """
        This function will check if the Rectangle fits the criteria of a square using top-left and bottom-right corners of the rectangle.
        It will return True or False.
        """
        print(inspect.getdoc(Rectangle.square()))
        if abs((self.t_top_left[0])-(self.t_bottom_right[0])) == (self.t_top_left[1])-(self.t_bottom_right[1]):
            return True
        else:
            return False

while True:
    print("\n\nThis program accepts input in the form of Direct Input from keyboard or ordered pairs ie. (2,6) (without parentheses)?")
    input_or_tuples = input('For direct input type "i" or "t" for tuples (without quotes) and press [ENTER]:\n')
    if input_or_tuples == 'i':
        length = float(input("\nInput length of the Rectangle: "))
        if isinstance(length, float):
            print("Length is float!")
        else:
            print("Length is not a float!")
        width = float(input("Input width of the Rectangle: "))
        if isinstance(width, float):
            print("Width is float!")
        else:
            print("Width is not a float!")
        tuple_length = 0
        tuple_width = 0
        print("\nPerimeter of Rectangle: ", Rectangle(length, width, tuple_length, tuple_width).perimeter_input())
        print("Area of Rectangle: ", Rectangle(length, width, tuple_length, tuple_width).area_input())
    elif input_or_tuples == 't':
        #top_left_x = float(input("\nInput x value for the top-left corner of the Rectangle: "))
        #top_left_y = float(input("\nInput y value for the top-left corner of the Rectangle: "))
        #top_left_tuple = (top_left_x, top_left_y)
        my_top_left_tuple = input('Enter a point (x,y) for the top-left corner of the Rectangle (without parentheses) and press [ENTER]: ')
        inList = [float(n) for n in my_top_left_tuple.split(',')]
        top_left_tuple = tuple(inList)

        #bottom_right_x = float(input("\nInput x value for the bottom-right corner of the Rectangle: "))
        #bottom_right_y = float(input("\nInput y value for the bottom-right corner of the Rectangle: "))
        #bottom_right_tuple = (bottom_right_x, bottom_right_y)
        my_bottom_right_tuple = input('Enter a point (x,y) for the bottom-right corner of the Rectangle (without parentheses) and press [ENTER]: ')
        inList = [float(n) for n in my_bottom_right_tuple.split(',')]
        bottom_right_tuple = tuple(inList)

        input_length = 0
        input_width = 0
        print("\nLength of Rectangle: ", Rectangle(input_length, input_width, top_left_tuple, bottom_right_tuple).length_tuple())
        print("Width of Rectangle: ", Rectangle(input_length, input_width, top_left_tuple, bottom_right_tuple).width_tuple())
        print("\nPerimeter of Rectangle: ", Rectangle(input_length, input_width, top_left_tuple, bottom_right_tuple).perimeter_tuple())
        print("Area of Rectangle: ", Rectangle(input_length, input_width, top_left_tuple, bottom_right_tuple).area_tuple())
        print("Does Rectangle fit criteria of a square? ", Rectangle(input_length, input_width, top_left_tuple, bottom_right_tuple).square())

    else:
        print("You entered invalid input!")