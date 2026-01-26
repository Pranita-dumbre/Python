#################################################
#  File name :     Question16_6.py
#  Descreption :   Used to display positive, negative and zero
#  Author :        Pranita Purushottam Dumbre
#  Date :          24/01/2026
##################################################
def Display(No):
    if(No > 0):
        print("Positive number")
    elif(No < 0):
        print("Negative number")
    else:
        print("It is zero")
     
def main():
    print("Enter the number : ")
    value = int(input())

    Display(value)   

if __name__ == "__main__":
    main()