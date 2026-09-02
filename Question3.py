def triangle():

    a = int(input("Enter first side of triangle: "))
    b = int(input("Enter second side of triangle: "))
    c = int(input("Enter third side of triangle: "))

    if (a>b and a>c):
        greatest = a

    elif (b>a and b>c):
        greatest = b

    else:
        greatest = c

    largest_side = greatest*greatest
    if greatest == a:
        if largest_side == b*b + c*c:
            print("It is a right angled triangle")
        else:
            print("It is not a right angled triangle")
    elif greatest == b:
        if largest_side == a*a + c*c:
            print("It is a right angled triangle")
        else:
            print("It is not a right angled triangle")
    elif greatest == c:
        if largest_side == a*a + b*b:
            print("It is a right angled triangle")
        else:
            print("It is not aright a right angled triangle")
triangle()