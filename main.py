import matplotlib.pyplot as plt
import pandas as pd


def load_csv(filename: str) -> pd.DataFrame:
    return pd.read_csv(filename)


def main():
    # loading .csv file
    filename = "data.csv"
    df = load_csv(filename)

    # dividing dataset into X and Y sets
    X = df['U']
    Y = df['a']

    # showing the correlation field
    plt.plot(X, Y, 'go')
    plt.title("Correlation field")
    plt.show()


if __name__ == '__main__':
    main()


