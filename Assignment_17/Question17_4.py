#################################################
#  File name :     Question17_4.py
#  Descreption :   Used to accept the one number from user display 
#                  addition of all factors          
#  Author :        Pranita Purushottam Dumbre
#  Date :          24/01/2026
##################################################
def SumFactor(No):
    Sum = 0
    for i in range(1,No):
        if (No % i == 0):
            Sum = Sum + i
    return Sum

def main():
    Ret = 0

    print("Enter number")
    Value = int(input())

    Ret = SumFactor(Value)

    print("Sum of factor is : ",Ret)

if __name__ == "__main__":
    main()