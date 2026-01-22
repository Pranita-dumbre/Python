#######################################
#  File name :     Question10_5.py
#  Descreption :   Used to accepts one number and 
#                   print all odd number till that number
#  Author :        Pranita Purushottam Dumbre
#  Date :          18/01/2026
#######################################
def OddNumber(Value):
    print("Odd Numbers are  : ")
    for i in range(1,Value + 1,2):
        print(i)
    
def main():

    print("Enter Number : ")
    No = int(input())

    OddNumber(No)
    
if __name__ == "__main__":
    main()