#######################################
#  File name :     Question11_5.py
#  Descreption :   Used to accepts one number and print check 
#                   wheter it is palindrome or not
#  Author :        Pranita Purushottam Dumbre
#  Date :          19/01/2026
#######################################
def Palindrome(No):
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

    Ret = Palindrome(Value)

    if(Ret == Value):
        print("Given number is Palindrome")
    else:
        print("Given number is not Plindrome")


if __name__ == "__main__":
    main()