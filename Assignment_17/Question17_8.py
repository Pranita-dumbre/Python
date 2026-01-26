#################################################
#  File name :     Question17_1.py
#  Descreption :   Used to display the matrix of * pattern              
#  Author :        Pranita Purushottam Dumbre
#  Date :          24/01/2026
##################################################
def Display(No):
    for i in range(1, No + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()
        

def main():
    print("Enter number")
    iSize = int(input())

    Display(iSize)

if __name__ == "__main__":
    main()

   