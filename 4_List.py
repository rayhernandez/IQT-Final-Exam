# Using lists, read in 30 numbers and print out whether the number read is a duplicate
# of a previous number.
import inspect


def find_duplicates():
    """
    This function will read in 30 numbers from a list and print out any duplicates.
    """
    print(inspect.getdoc(find_duplicates))
    my_list = (1, 2, 2, 4, 5, 6, 7, 8, 8, 10, 11, 12, 13, 14, 14, 16, 17, 18, 19, 19, 21, 22, 22, 24, 25, 26, 27, 28, 28, 30)
    while True:
        for i in range(len(my_list[1:])):   # "my_list[1:]" will skip the first element of the list since there isn't a prev number.
            #if my_list[i] == my_list[i+i]:
            if my_list[i] == my_list[i+1]:
            #print("Comparing...current Number", my_list[i+i], "to previous", my_list[i], "DUPLICATE FOUND!")
                print("Searching list for duplicates...", my_list[i+1], "DUPLICATE FOUND!")
            ##elif my_list[i] != my_list[i+i]:
            # elif my_list[i] != my_list[i+1]:
            # #print("Comparing...current Number", my_list[i+i], "to previous", my_list[i], "NOT Found")
            #     print("Comparing...", my_list[i] != my_list[i+1], "NOT Found")
        break
print(find_duplicates())
