#################################################
#  File name :     Question16_7.py
#  Descreption :   Used to display check divixible by 5 or not
#  Author :        Pranita Purushottam Dumbre
#  Date :          24/01/2026
##################################################
def Check(No):
    if(No % 5 == 0):
        return True
    else:
        return False
     
def main():
    Ret = False

    print("Enter the number : ")
    value = int(input())

    Ret = Check(value)   

    print(Ret)

if __name__ == "__main__":
    main()

    