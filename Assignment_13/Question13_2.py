#################################################
#  File name :     Question13_2.py
#  Descreption :   Used to accepts radius and
#                  print area of circle.
#  Author :        Pranita Purushottam Dumbre
#  Date :          19/01/2026
##################################################
PI = 3.14

def CircleArea(radius):
    Area = 0
    Area = PI * (radius * radius)
    return Area
    
def main():
    Ret = 0

    print("Enter radius of cirle : ")
    Radius = int(input())

    Ret = CircleArea(Radius)

    print("Area of rectangle is : ",Ret)
    
if __name__ == "__main__":
    main()