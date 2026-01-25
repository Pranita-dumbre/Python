#################################################
#  File name :     Question14_4.py
#  Descreption :   Used to accepts 2 numbers & print
#                  Minimum number using lambda function
#  Author :        Pranita Purushottam Dumbre
#  Date :          21/01/2026
##################################################
Minimum = lambda No1 ,No2 : (No1 < No2)
def main():
    Ret = 0
    print("Enter first no : ")
    Value1 = int(input())

    print("Enter second no : ")
    Value2 = int(input())

    Ret = Minimum(Value1,Value2)

    if (Ret == True):
        print("Minimum number is : ",Value1)
    else:
        print("Minimum number is : ",Value2)

if __name__ == "__main__":
    main()