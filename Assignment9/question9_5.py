#######################################
#  File name :     Question9_3.py
#  Descreption :   Used to accepts one number and 
#                   check whether divisible by 3 and 5
#  Author :        Pranita Purushottam Dumbre
#  Date :          17/01/2026
#######################################

def Divisible(Value):
    if ((Value % 3 == 0) and (Value % 5 == 0)):
        return True
    else:
        return False
    
def main():
    Ret = False

    print("Enter Number : ")
    No = int(input())

    Ret = Divisible(No)

    if(Ret == True):
        print(No,"is Divisible by 3 and  5")
    else:
        print(No,"is not Divisible by 3 and  5")
    
if __name__ == "__main__":
    main()