def Prime(Value):

    if(Value % 2 == 0):
        return False
    else:
        return True
    
def main():
    Ret = False

    print("Enter Number : ")
    No = int(input())

    Ret = Prime(No)

    if(Ret == True):
        print("Number is Prime")
    else:
        print("Number is Not Prime")

    
if __name__ == "__main__":
    main()