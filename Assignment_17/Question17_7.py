#################################################
#  File name :     Question17_7.py
#  Descreption :   Used to display the pattern              
#  Author :        Pranita Purushottam Dumbre
#  Date :          24/01/2026
##################################################
def Display(No):
    for i in range(No):
        for j in range(1, No + 1):
            print(j, end="")
        print()
        
def main():
    print("Enter number")
    iSize = int(input())

    Display(iSize)

if __name__ == "__main__":
    main()

    