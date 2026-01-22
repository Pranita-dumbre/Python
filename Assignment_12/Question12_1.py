#################################################
#  File name :     Question12_1.py
#  Descreption :   Used to accepts one charactor and 
#                  check it is vowle or consonant.
#  Author :        Pranita Purushottam Dumbre
#  Date :          19/01/2026
##################################################
def Vowels(Arr):
    if ((Arr == "a") | (Arr == "e") | (Arr == "i") | (Arr == "o") | (Arr == "u")):
        return True
    else:
        return False
    
def main():
    Ret = False

    print("Enter Number : ")
    Str = input()

    Ret = Vowels(Str)

    if(Ret == True):
        print("Its is Vowle")
    else:
        print("It is  Consonant")


if __name__ == "__main__":
    main()