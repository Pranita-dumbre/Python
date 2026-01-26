def SumDigits(No):
    Sum = 0
    while (No != 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    return Sum


def main():
    print("Enter number:")
    Value = int(input())

    Ret = SumDigits(Value)
    print("Sum of digits is:", Ret)


if __name__ == "__main__":
    main()
