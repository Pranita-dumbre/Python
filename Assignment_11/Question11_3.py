#######################################
#  File name :     Question11_3.py
#  Descreption :   Used to accepts one number and 
#                   print sum of digit.
#  Author :        Pranita Purushottam Dumbre
#  Date :          19/01/2026
#######################################
def SumDigit(No):
    iDigit = 0
    Sum = 0
    while(No != 0):

        iDigit = No % 10
        Sum = Sum + iDigit
        No = No // 10
    return Sum
    
def main():
    Ret = 0

    print("Enter Number : ")
    Value = int(input())

    Ret = SumDigit(Value)

    print("The sum of all Digit in ",Value,"is : ",Ret)

    
if __name__ == "__main__":
    main()