import threading

def Maximum(Arr):
    temp = Arr[1]

    for i in range(1,len(Arr)):
        if(Arr[i]> temp):
            temp = Arr[i]
    print("Minimum element :",temp)



def Minimum(Arr):
    temp = Arr[1]

    for i in range(1,len(Arr)):
        if(Arr[i]< temp):
            temp = Arr[i]
    print("Minimum element :",temp)

def main():
    print("Enter the number of elements : ")
    Size = int(input())

    Data = []

    print("Enter elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    t1 = threading.Thread(target=Maximum,args=(Data,))
    t2 = threading.Thread(target=Minimum,args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
