#################################################
#  File name :     Question14_5.py
#  Descreption :   Used to accepts 1 number & print
#                  Even-Odd number using lambda function
#  Author :        Pranita Purushottam Dumbre
#  Date :          21/01/2026
##################################################
Even = lambda no : (no % 2 == 0)

def main():
    Ret = 0
    print("Enter the number : ")
    No = int(input())

    Ret = Even(No)

    print(Ret)

    if (Ret == True):
        print("Number is Even")
    else:
        print("Number is Odd")

    
if __name__ == "__main__":
    main()