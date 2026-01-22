#######################################
#  File name :     Question10_3.py
#  Descreption :   Used to accepts one number and 
#                   print Factorical of that number
#  Author :        Pranita Purushottam Dumbre
#  Date :          17/01/2026
#######################################
def Factorical(Value):
    Ans = 1

    for i in range(1,Value + 1):
        Ans = Ans * i
    return Ans
    
def main():
    Ret = 0

    print("Enter Number : ")
    No = int(input())

    Ret = Factorical(No)

    print("Addition is : ",Ret)
    
if __name__ == "__main__":
    main()