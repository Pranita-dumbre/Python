#################################################
#  File name :     Question15_2.py
#  Descreption :   Write a lambda function using filter which accept list of 
#                  numbers and return the list of even numbers
#  Author :        Pranita Purushottam Dumbre
#  Date :          23/01/2026
##################################################

def main():
    print("Enter the element count :")
    Size = int(input())

    Data = []

    print("Enter the elements:")
    for i in range(Size):
        value = int(input())
        Data.append(value)
    print("The Actual data is : ",Data)

    Fdata = list(filter(lambda No : No % 2 == 0 ,Data))

    print("Even number is :",Fdata)

if __name__ == "__main__":
    main()