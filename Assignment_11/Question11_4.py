#######################################
#  File name :     Question11_2.py
#  Descreption :   Used to accepts one number and 
#                   print reverse of that number.
#  Author :        Pranita Purushottam Dumbre
#  Date :          19/01/2026
#######################################
def DigitCount(No):
    iDigit = 0
    Rev = 0
    while(No != 0):

        Digit = No % 10
        Rev = (Rev * 10) + Digit
        No = No // 10
    return Rev
    
def main():
    Ret = 0

    print("Enter Number : ")
    Value = int(input())

    Ret = DigitCount(Value)

    print("The revrse number is : ",Ret)

if __name__ == "__main__":
    main()