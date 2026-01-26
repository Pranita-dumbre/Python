#################################################
#  File name :     Question16_2.py
#  Descreption :   Used to check number is even or odd
#  Author :        Pranita Purushottam Dumbre
#  Date :          24/01/2026
##################################################
def ChkNum(No):
    if No % 2 == 0:
        return True
    else:
        return False
    
def main():
    Ret = False
    print("Enter the number : ")
    value = int(input())

    Ret = ChkNum(value)
    if (Ret == True):
        print("Even Numbre")
    else:
        print("Odd numbre")

if __name__ == "__main__":
    main()