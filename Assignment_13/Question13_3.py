#################################################
#  File name :     Question13_3.py
#  Descreption :   Used to accepts one number and 
#                  print Sum of  factors.
#  Author :        Pranita Purushottam Dumbre
#  Date :          19/01/2026
##################################################
def SumFactor(Value):
    Sum = 0

    for i in range (1,Value):
        
        if(Value % i == 0):
            Sum = Sum + i
    return Sum
    
def main():

    Ret = 0

    print("Enter Number : ")
    No = int(input())

    Ret = SumFactor(No)

    if(Ret == No):
        print("Number is Perfact Number")
    else:
        print("Number is not Perfact Number")

    
if __name__ == "__main__":
    main()