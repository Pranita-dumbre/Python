#################################################
#  File name :     Question14_2.py
#  Descreption :   Used to accepts one number and 
#                  print cube of no. using lambda function
#  Author :        Pranita Purushottam Dumbre
#  Date :          21/01/2026
##################################################
Cube = lambda no : ( no ** 3 )

def main():
    Ret = 0
    print("Enter the number : ")
    No = int(input())

    Ret = Cube(No)

    print("Cube is : ",Ret)

if __name__ == "__main__":
    main()