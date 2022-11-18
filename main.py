import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def load_csv(filename: str) -> pd.DataFrame:
    return pd.read_csv(filename)


def main():
    # loading .csv file
    filename = "data.csv"
    df = load_csv(filename)

    # dividing dataset into X and Y sets
    X = df['U']
    Y = df['a']

    y_max = Y.max()
    x_max = X.max()
    x_threshold_value = X.mean()
    y_threshold_value = Y.mean()

    # showing the correlation field
    plt.plot(X, Y, 'go')
    plt.plot(np.full(2, x_threshold_value), [0, y_max])
    plt.plot([0, x_max], np.full(2, y_threshold_value))
    plt.title("Correlation field")
    plt.show()


if __name__ == '__main__':
    main()


