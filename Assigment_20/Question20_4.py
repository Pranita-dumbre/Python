import threading

def Small():
    Str = "MarVeLlouS123"
    Count = 0
    for ch in Str:
        if ch.islower():
            Count = Count + 1
    print("Lowercase count:", Count)
    print("Thread Name:", threading.current_thread().name)
    print("Thread ID:", threading.get_ident())


def Capital():
    Str = "MarVeLlouS123"
    Count = 0
    for ch in Str:
        if ch.isupper():
            Count = Count + 1
    print("Uppercase count:", Count)
    print("Thread Name:", threading.current_thread().name)
    print("Thread ID:", threading.get_ident())


def Digits():
    Str = "MarVeLlouS123"
    Count = 0
    for ch in Str:
        if ch.isdigit():
            Count = Count + 1
    print("Digit count:", Count)
    print("Thread Name:", threading.current_thread().name)
    print("Thread ID:", threading.get_ident())


def main():
    t1 = threading.Thread(target=Small, name="Small")
    t2 = threading.Thread(target=Capital, name="Capital")
    t3 = threading.Thread(target=Digits, name="Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


if __name__ == "__main__":
    main()
