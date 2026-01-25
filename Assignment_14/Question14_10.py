#################################################
#  File name :     Question14_10.py
#  Descreption :   Used to accepts 3 numbers & print
#                  largest number using lambda function
#  Author :        Pranita Purushottam Dumbre
#  Date :          21/01/2026
##################################################

Addition = lambda No1 ,No2 : No1 > No2 

def main():
    Ret = 0
    print("Enter first no : ")
    Value1 = int(input())

    print("Enter second no : ")
    Value2 = int(input())

    print("Enter third no : ")
    Value3 = int(input())


    Ret = Addition(Value1,Value2)

    if  Ret == False:
        Ret2 = Value2
    else:
        Ret2 = Value1


    Ret1 = Addition(Ret2,Value3)

    if Ret1 == True:
        print("Larger value is : ",Value2)
    else:
        print("Larger value is : ",Value3)

if __name__ == "__main__":
    main()