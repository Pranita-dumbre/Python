#######################################
#  File name :     Question9_4.py
#  Descreption :   Used to accepts one number and 
#                   display the cube of that number
#  Author :        Pranita Purushottam Dumbre
#  Date :          17/01/2026
#######################################

def Cube(Value):
    Ans = 0
    Ans = Value ** 3
    return Ans
    
def main():
    Ret = 0

    print("Enter Number : ")
    No = int(input())

    Ret = Cube(No)

    print("Cube of ",No,"is",Ret)
    
if __name__ == "__main__":
    main()