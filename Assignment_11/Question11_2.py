#######################################
#  File name :     Question11_2.py
#  Descreption :   Used to accepts one number and 
#                   print count of digit in it.
#  Author :        Pranita Purushottam Dumbre
#  Date :          19/01/2026
#######################################
def DigitCount(No):
    iDigit = 0
    i = 0
    while(No != 0):

        iDigit = No % 10
        i = i + 1
        No = No // 10
    return i
    
def main():
    Ret = 0

    print("Enter Number : ")
    Value = int(input())

    Ret = DigitCount(Value)

    print("The count of  Digit in ",Value,"is : ",Ret)

    
if __name__ == "__main__":
    main()