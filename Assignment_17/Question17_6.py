#################################################
#  File name :     Question17_1.py
#  Descreption :   Used to display the matrix of * pattern              
#  Author :        Pranita Purushottam Dumbre
#  Date :          24/01/2026
##################################################
def Display(No):

    for i in range(No, 0, -1):
        print("*" * i)

def main():
    print("Enter number")
    iSize = int(input())

    Display(iSize)

if __name__ == "__main__":
    main()

    