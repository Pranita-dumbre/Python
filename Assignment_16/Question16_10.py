#################################################
#  File name :     Question16_10.py
#  Descreption :   Used to accept name from user and display the length                
#  Author :        Pranita Purushottam Dumbre
#  Date :          24/01/2026
##################################################
def length(Arr):
    Count = 0
    for i in range(len(Arr)):
        Count = Count + 1
    return Count
     
def main():
    Ret = 0

    print("Enter the string : ")
    str = input()
    
    Ret = length(str)  

    print(Ret) 

if __name__ == "__main__":
    main()