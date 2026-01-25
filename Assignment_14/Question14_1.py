#################################################
#  File name :     Question14_1.py
#  Descreption :   Used to accepts one number and 
#                  print square of no. using lambda function
#  Author :        Pranita Purushottam Dumbre
#  Date :          21/01/2026
##################################################
Square = lambda no : ( no * no )

def main():
    Ret = 0
    print("Enter the number : ")
    No = int(input())

    Ret = Square(No)

    print("Square is : ",Ret)

if __name__ == "__main__":
    main()