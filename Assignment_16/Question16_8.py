#################################################
#  File name :     Question16_8.py
#  Descreption :   Used to display number of "*" 
#  Author :        Pranita Purushottam Dumbre
#  Date :          24/01/2026
##################################################
def Display(No):
    print(" * " * No)
     
def main():

    print("Enter the number : ")
    iSize = int(input())

    Ret = Display(iSize)   

if __name__ == "__main__":
    main()