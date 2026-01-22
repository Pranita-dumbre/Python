#################################################
#  File name :     Question12_2.py
#  Descreption :   Used to accepts one number and 
#                  print it's factor
#  Author :        Pranita Purushottam Dumbre
#  Date :          19/01/2026
##################################################
def Factor(Value):
    print("Factors is : ")
    for i in range (1,Value+1):
        if(Value % i == 0):
            print(i)
    
def main():

    print("Enter Number : ")
    No = int(input())

    Factor(No)
    
if __name__ == "__main__":
    main()