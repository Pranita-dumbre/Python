#######################################
#  File name :     Question9_3.py
#  Descreption :   Used to accepts one number and 
#                   display the square of that number
#  Author :        Pranita Purushottam Dumbre
#  Date :          17/01/2026
#######################################

def Square(Value):
    square = 0
    square = Value * Value
    return square
    
def main():
    Ret = 0

    print("Enter Number : ")
    No = int(input())

    Ret = Square(No)

    print("Square of ",No,"is",Ret)
    
if __name__ == "__main__":
    main()