from sklearn.metrics import classification_report

def Confusion_matrix(actual,predicted):

    TP = 0
    TN = 0
    FP = 0
    FN = 0

    for a,p in zip(actual,predicted):

        if a==1 and p==1:
            TP = TP + 1

        elif a==0 and p==0:
            TN = TN + 1

        elif a==0 and p==1:
            FP = FP + 1

        elif a==1 and p==0:
            FN = FN + 1

    print("True Positive:",TP)
    print("True Negative:",TN)
    print("False Positive:",FP)
    print("False Negative:",FN)


def main():

    actual = [1,1,1,1,0,0,0,0]
    predicted = [1,1,0,1,0,1,0,0]

    Confusion_matrix(actual,predicted)

    print("\nClassification Report:\n")
    print(classification_report(actual,predicted))


if __name__ == "__main__":
    main()