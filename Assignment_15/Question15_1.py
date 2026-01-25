#################################################
#  File name :     Question15_1.py
#  Descreption :   Write a lambda function using map() which accepted
#                  list of number and return the square of that number
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

    Mdata = list(map(lambda Arr : Arr * Arr,Data))

    print("Suqare of each elements is :",Mdata)

if __name__ == "__main__":
    main()