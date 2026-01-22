#######################################
#  File name :     Question10_1.py
#  Descreption :   Used to accepts one number and 
#                   print multiplication table of that number
#  Author :        Pranita Purushottam Dumbre
#  Date :          17/01/2026
#######################################

def Table(Value):

    for i in range(1,11):
        print(Value,"X",i,"=",Value * i)
    
def main():

    print("Enter Number : ")
    No = int(input())

    Table(No)
    
if __name__ == "__main__":
    main()