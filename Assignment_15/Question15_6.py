#################################################
#  File name :     Question15_6.py
#  Descreption :   Write a lambda function using reduce() which accept list of 
#                  numbers and return the minimum element
#  Author :        Pranita Purushottam Dumbre
#  Date :          23/01/2026
##################################################
from functools import reduce

def main():
    print("Enter the element count :")
    Size = int(input())

    Data = []

    print("Enter the elements:")
    for i in range(Size):
        value = int(input())
        Data.append(value)
    print("The data is : ",Data)

    Fdata = int(reduce(lambda a, b: (a < b) and a or b,Data))

    print(Fdata)


if __name__ == "__main__":
    main()