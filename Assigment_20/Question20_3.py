import threading

def EvenList(Data):
    Sum = 0
    print("Even elements:")
    for i in Data:
        if i % 2 == 0:
            print(i)
            Sum = Sum + i
    print("Sum of even elements:", Sum)


def OddList(Data):
    Sum = 0
    print("Odd elements:")
    for i in Data:
        if i % 2 != 0:
            print(i)
            Sum = Sum + i
    print("Sum of odd elements:", Sum)


def main():
    print("Enter the number of elements : ")
    Size = int(input())

    Data = list()

    print("Enter elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)


    t1 = threading.Thread(target=EvenList, args=(Data,))
    t2 = threading.Thread(target=OddList, args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
