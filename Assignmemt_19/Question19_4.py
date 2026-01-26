from functools import reduce 

def main():
    print("Nymber of elements :")
    Size = int(input())

    Data = list()

    print("Enter elements :")
    for i in range(Size):
        value = int(input())
        Data.append(value)
    print("The Actual data is : ",Data)

    Fdata = list(filter(lambda Arr : Arr % 2 == 0 ,Data))

    print(Fdata)

    Mdata = list(map(lambda Brr : Brr ** 2,Fdata))

    print(Mdata)

    Rdata = int(reduce(lambda A , B : A + B,Mdata))

    print(Rdata)


if __name__ == "__main__":
    main()