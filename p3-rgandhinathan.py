#  This program compares three integers and figures out which one is the greatest
#  When a non-integer value is given it will throw out "Invalid Input! Enter valid integers"


#  This function compares which of the three integer is the greatest
def maxofthree(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z


try:
    a = input("Enter first value:")
    b = input("Enter second value: ")
    c = input("Enter third value:")
    a = int(a)
    b = int(b)
    c = int(c)
    max_num = maxofthree(a, b, c)
    print("The maximum of", a, b, c, "is", max_num)
except ValueError:
    #  When the user enters non-integer value this starts to execute
    print("Invalid Input! Enter valid integers")
