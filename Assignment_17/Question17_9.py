def DigitCount(No):
    Count = 0
    while No != 0:
        Count = Count + 1
        No = No // 10
    return Count


def main():
    print("Enter number:")
    Value = int(input())

    Ret = DigitCount(Value)
    print("Number of digits are:", Ret)


if __name__ == "__main__":
    main()
