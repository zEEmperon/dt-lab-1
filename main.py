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

    dec_K1_div_K1 = df[(df['U'] <= x_threshold_value) & (df['a'] <= y_threshold_value)]
    dec_K1_div_K2 = df[(df['U'] <= x_threshold_value) & (df['a'] > y_threshold_value)]
    dec_K2_div_K2 = df[(df['U'] > x_threshold_value) & (df['a'] > y_threshold_value)]
    dec_K2_div_K1 = df[(df['U'] > x_threshold_value) & (df['a'] <= y_threshold_value)]

    # showing the correlation field
    plt.plot(dec_K1_div_K1['U'], dec_K1_div_K1['a'], 'go', label='ріш К1 / К1')
    plt.plot(dec_K1_div_K2['U'], dec_K1_div_K2['a'], 'ro', label='ріш К1 / К2')
    plt.plot(dec_K2_div_K2['U'], dec_K2_div_K2['a'], 'bo', label='ріш К2 / К2')
    plt.plot(dec_K2_div_K1['U'], dec_K2_div_K1['a'], 'yo', label='ріш К2 / К1')

    plt.plot(np.full(2, x_threshold_value), [0, y_max])
    plt.plot([0, x_max], np.full(2, y_threshold_value))

    plt.title("Correlation field")
    plt.legend()

    plt.show()


if __name__ == '__main__':
    main()


