import pandas as pd
from sklearn.linear_model import LinearRegression

def main():

    X = pd.DataFrame({
        "Study_Hours":[1,2,3,4,5]
    })

    Y = [50,55,60,65,70]

    new_data = pd.DataFrame({
        "Study_Hours":[6]
    })

    model = LinearRegression()

    model.fit(X,Y)

    for column, value in zip(X.columns, model.coef_):
        print(f"{column} : {value}")

    print("Intercept :",model.intercept_)

    Y_pred = model.predict(new_data)

    print("Predicted Marks for 6 study hours:",Y_pred)

if __name__ == "__main__":
    main()