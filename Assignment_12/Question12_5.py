#################################################
#  File name :     Question12_5.py
#  Descreption :   Used to accepts one number and 
#                  print many numbres in rverse order
#  Author :        Pranita Purushottam Dumbre
#  Date :          19/01/2026
##################################################
def Display(Value):
    
    for i in range (Value,0,-1):
        print(i)
    
def main():

    print("Enter Number : ")
    No = int(input())

    Display(No)
    
if __name__ == "__main__":
    main()