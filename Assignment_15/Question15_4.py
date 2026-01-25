#################################################
#  File name :     Question15_4.py
#  Descreption :   Write a lambda function using reduce() which accept list of 
#                  numbers and return the addition of all elements
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
    print("The Actual data is : ",Data)

    Rdata = int(reduce(lambda A , B : A + B,Data))

    print("Summation of all elements are :",Rdata)

if __name__ == "__main__":
    main()