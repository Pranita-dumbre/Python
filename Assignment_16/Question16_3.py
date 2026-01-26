#################################################
#  File name :     Question16_3.py
#  Descreption :   Used to accepts two number and 
#                  print addition of two numbres.
#  Author :        Pranita Purushottam Dumbre
#  Date :          24/01/2026
##################################################
def Add(No1, No2):
    Ans = 0
    Ans = No1 + No2
    return Ans
    
def main():
    Ret = False
    print("Enter first number : ")
    value1 = int(input())

    print("Enter second number : ")
    value2 = int(input())

    Ret = Add(value1,value2)
    
    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()