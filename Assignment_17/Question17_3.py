#################################################
#  File name :     Question17_3.py
#  Descreption :   Used to accept the one number from user display 
#                  addition of all factors          
#  Author :        Pranita Purushottam Dumbre
#  Date :          24/01/2026
##################################################
def Factorial(No):
    Fact = 1
    for i in range(1, No + 1):
        Fact = Fact * i
    return Fact

def main():
    Ret = 0

    print("Enter number")
    Value = int(input())

    Ret = Factorial(Value)

    print("Factorical is : ",Ret)

if __name__ == "__main__":
    main()