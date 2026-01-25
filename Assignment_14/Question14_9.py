#################################################
#  File name :     Question14_8.py
#  Descreption :   Used to accepts 2 numbers & print
#                  Multiplication using lambda function
#  Author :        Pranita Purushottam Dumbre
#  Date :          21/01/2026
##################################################
Addition = lambda No1 ,No2 : (No1 * No2)

def main():
    Ret = 0
    print("Enter first no : ")
    Value1 = int(input())

    print("Enter second no : ")
    Value2 = int(input())

    Ret = Addition(Value1,Value2)

    print("Multiplication  is : ",Ret)

if __name__ == "__main__":
    main()