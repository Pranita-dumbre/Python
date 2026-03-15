import numpy as np
import math

from sklearn.preprocessing import StandardScaler

def EucDistance(P1,P2):
    Ans = math.sqrt((P1[0] - P2[0])**2 + (P1[1] - P2[1])**2)
    return Ans

def main():
    Border = "=" * 50

    data = np.array([
        [25,20000],
        [30,40000],
        [35,80000]
    ])

    print(Border)
    print("Before Scaling")
    print(Border)
    Result = EucDistance(data[0],data[1])
    print("Distance before scaling:",Result)

    scaler = StandardScaler()

    scaled_data = scaler.fit_transform(data)
    print(Border)
    print("Scaled Dataset:")
    print(Border)
    print(scaled_data)

    print(Border)
    print("After Scaling")
    print(Border)
    Result1 = EucDistance(scaled_data[0],scaled_data[1])
    print("Distance after scaling:",Result)
if __name__ == "__main__":
    main()