import threading

def Prime(Data):
    print("Prime numbers:")
    for No in Data:
        if No > 1:
            Flag = True
            for i in range(2, No):
                if No % i == 0:
                    Flag = False
                    break
            if Flag:
                print(No)


def NonPrime(Data):
    print("Non-prime numbers:")
    for No in Data:
        if No <= 1:
            print(No)
        else:
            Flag = False
            for i in range(2, No):
                if No % i == 0:
                    Flag = True
                    break
            if Flag:
                print(No)


def main():
    print("Enter the number of elements : ")
    Size = int(input())

    Data = []

    print("Enter elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    t1 = threading.Thread(target=Prime, args=(Data,))
    t2 = threading.Thread(target=NonPrime, args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
