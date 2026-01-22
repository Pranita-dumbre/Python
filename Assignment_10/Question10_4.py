def EvenNumber(Value):
    print("Even Numbers are  : ")
    for i in range(2,Value + 1,2):
        print(i)
    
def main():

    print("Enter Number : ")
    No = int(input())

    EvenNumber(No)
    
if __name__ == "__main__":
    main()