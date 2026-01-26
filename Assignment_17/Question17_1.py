#################################################
#  File name :     Question17_1.py
#  Descreption :   Used to accept 2 input from user perfrom opreation using module                
#  Author :        Pranita Purushottam Dumbre
#  Date :          24/01/2026
##################################################
import Arithmatic

def main():
    print("Enter first number")
    Value1 = int(input())

    print("Enter second number")
    Value2 = int(input())

    Ret = Arithmatic.Addition(Value1,Value2)
    print("Addition is : ",Ret)

    Ret = Arithmatic.Subraction(Value1,Value2)
    print("Subraction is : ",Ret)

    Ret = Arithmatic.Multiplication(Value1,Value2)
    print("Multiplication is : ",Ret)

    Ret = Arithmatic.Division(Value1,Value2)
    print("Division is : ",Ret)


if __name__ == "__main__":
    main()