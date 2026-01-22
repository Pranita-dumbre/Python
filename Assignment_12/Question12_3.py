#################################################
#  File name :     Question12_3.py
#  Descreption :   Used to accepts two number and 
#                  print add,sub, multi and division
#  Author :        Pranita Purushottam Dumbre
#  Date :          19/01/2026
##################################################
Addition = lambda Value1,Value2 : Value1 + Value2

Subtraction = lambda Value1,Value2 : Value1 - Value2

Division = lambda Value1,Value2 : Value1 / Value2

Multipication = lambda Value1,Value2 : Value1 * Value2
    
def main():

    Result1 = 0
    Result2 = 0
    Result3 = 0
    Result4 = 0


    print("Enter first Number : ")
    No1 = int(input())

    print("Enter first Number : ")
    No2 = int(input())
    
    Result1 = Addition(No1,No2)
    print("Addition is : ",Result1)

    Result2 = Subtraction(No1,No2)
    print("Subtraction is : ",Result2)

    Result3 = Multipication(No1,No2)
    print("Multipication is : ",Result3)

    Result4 = Division(No1,No2)
    print("Division is : ",Result4)

    
    
if __name__ == "__main__":
    main()