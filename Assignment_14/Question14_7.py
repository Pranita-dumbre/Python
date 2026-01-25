#################################################
#  File name :     Question14_6.py
#  Descreption :   aAccepts 1 number & print id no. is divisible
#                  by 5 return True otherwise False using lambda function
#  Author :        Pranita Purushottam Dumbre
#  Date :          21/01/2026
##################################################
CheckDivisible = lambda no : (no % 5 == 0)

def main():
    Ret = 0
    print("Enter the number : ")
    No = int(input())

    Ret = CheckDivisible(No)

    print(Ret)

    if (Ret == True):
        print("Number is divisible by 5")
    else:
        print("Number is not divisible by 5")

    
if __name__ == "__main__":
    main()