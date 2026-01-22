#################################################
#  File name :     Question12_2.py
#  Descreption :   Used to accepts one number and 
#                  print that many numbers starting with 1
#  Author :        Pranita Purushottam Dumbre
#  Date :          19/01/2026
##################################################
def Display(Value):
    
    for i in range (1,Value+1):
        print(i)
    
def main():

    print("Enter Number : ")
    No = int(input())

    Display(No)
    
if __name__ == "__main__":
    main()