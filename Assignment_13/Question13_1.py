#################################################
#  File name :     Question13_1.py
#  Descreption :   Used to accepts length and widhth and 
#                  print area od retangle.
#  Author :        Pranita Purushottam Dumbre
#  Date :          19/01/2026
##################################################
def RectArea(len,width):
    Area = 0
    Area = len * width
    return Area
    
def main():
    Ret = 0

    print("Enter length of rectangle : ")
    length = int(input())

    print("Enter width of rectangle : ")
    width = int(input())

    Ret = RectArea(length,width)

    print("Area of rectangle is : ",Ret)
    
if __name__ == "__main__":
    main()