#################################################
#  File name :     Question14_6.py
#  Descreption :   Used to accepts 1 number & print
#                  Even-Odd number using lambda function
#  Author :        Pranita Purushottam Dumbre
#  Date :          21/01/2026
##################################################
Odd = lambda no : (no % 2 != 0)

def main():
    Ret = 0
    print("Enter the number : ")
    No = int(input())

    Ret = Odd(No)

    print(Ret)

    if (Ret == True):
        print("Number is Odd")
    else:
        print("Number is Even")

    
if __name__ == "__main__":
    main()