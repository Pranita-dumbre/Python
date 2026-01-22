#######################################
#  File name :     Question10_2.py
#  Descreption :   Used to accepts one number and 
#                   print Sum of first N natural number
#  Author :        Pranita Purushottam Dumbre
#  Date :          17/01/2026
#######################################
def SumOfNum(Value):
    Ans = 0

    for i in range(1,Value + 1):
        Ans = Ans + i
    return Ans
    
def main():
    Ret = 0

    print("Enter Number : ")
    No = int(input())

    Ret = SumOfNum(No)

    print("Addition is : ",Ret)
    
if __name__ == "__main__":
    main()