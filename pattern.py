# https://prepinsta.com/pattern-programs-tutorial/


# def Square_Star_Pattern():
#     n = int(input("Enter Number of rows"))

#     for i in range(0, n):
#         print("*"*n)

# Square_Star_Pattern()


# def Hollow_Square_Star_Pattern():
#     n = int(input("Enter Number of rows"))

#     for i in range(0, n):
#         print("*"*n)

# Hollow_Square_Star_Pattern()


# def Right_Angle_Triangle_Pattern():
#     n = int(input("Enter Number of rows"))
#     for i in range(0, n):
#         print(" " * (n-(i+1)), end="")
#         print("*" * (i+1))
# Right_Angle_Triangle_Pattern()


# def Right_Angle_Triangle_Pattern():
#     n = int(input("Enter Number of rows"))
#     for i in range(0, n):
#         print("*" * (i+1))
# Right_Angle_Triangle_Pattern()


def Pyramid_Star_Pattern():
    n = int(input("Enter Number of rows"))
    k = 1
    for i in range(0, n):
        print(" "* (n-(i+1)), end="")
        print("*"*(k))
        k += 2

Pyramid_Star_Pattern()