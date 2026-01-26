import threading

def EvenFactor(No):
    Sum = 0
    print("Even factors are:")

    for i in range(1, No + 1):
        if No % i == 0 and i % 2 == 0:
            print(i)
            Sum = Sum + i
    print("Sum of even factors:", Sum)


def OddFactor(No):
    Sum = 0
    print("Odd factors are:")
    for i in range(1, No + 1):
        if No % i == 0 and i % 2 != 0:
            print(i)
            Sum = Sum + i
    print("Sum of odd factors:", Sum)


def main():
    print("Enter the number : ")
    Value = int(input())

    t1 = threading.Thread(target=EvenFactor, args=(Value,))
    t2 = threading.Thread(target=OddFactor, args=(Value,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()
