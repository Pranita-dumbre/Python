import threading

def Sumelements(Arr, result):
    Sum = 0
    for i in range(len(Arr)):
        Sum = Sum + Arr[i]
    result.append(Sum)

def Product(Arr, result):
    Mul = 1
    for i in range(len(Arr)):
        Mul = Mul *Arr[i]
    result.append(Mul)

def main():
    print("Enter the number of elements : ")
    Size = int(input())

    Data = []

    print("Enter elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    sum = []
    prod = []

    t1 = threading.Thread(target=Sumelements, args=(Data, sum))
    t2 = threading.Thread(target=Product, args=(Data, prod))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of elements:", sum[0])
    print("Product of elements:", prod[0])

if __name__ == "__main__":
    main()
