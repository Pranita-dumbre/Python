#######################################
#  File name :     Question9_2.py
#  Descreption :   Used to accepts two number and display the maximum number
#  Author :        Pranita Purushottam Dumbre
#  Date :          17/01/2026
#######################################
def CheckGreater(Value1, Value2):
    if(Value1 > Value2):
        return Value1
    else:
        return Value2
    
def main():
    Ret = 0

    print("Enter first no : ")
    No1 = int(input())

    print("Enter second no : ")
    No2 = int(input())

    Ret = CheckGreater(No1, No2)

    print("The Grater number between ",No1,",",No2,"is",Ret)
    
if __name__ == "__main__":
    main()