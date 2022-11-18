from tabulate import tabulate
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

    n = len(df)
    y_max = Y.max()
    x_max = X.max()
    x_threshold_value = X.mean()
    y_threshold_value = Y.mean()

    dec_K1_div_K1 = df[(df['U'] <= x_threshold_value) & (df['a'] <= y_threshold_value)]
    dec_K1_div_K2 = df[(df['U'] <= x_threshold_value) & (df['a'] > y_threshold_value)]
    dec_K2_div_K2 = df[(df['U'] > x_threshold_value) & (df['a'] > y_threshold_value)]
    dec_K2_div_K1 = df[(df['U'] > x_threshold_value) & (df['a'] <= y_threshold_value)]
    dec_K1 = df[df['U'] <= x_threshold_value]
    dec_K2 = df[df['U'] > x_threshold_value]
    K1 = df[df['a'] <= y_threshold_value]
    K2 = df[df['a'] > y_threshold_value]

    p_K1_div_dec_K2 = len(dec_K1_div_K2) / len(dec_K1)
    p_K2_div_dec_K1 = len(dec_K2_div_K1) / len(dec_K2)
    p_dec_K1_div_K2 = len(dec_K1_div_K2) / len(K2)
    p_dec_K2_div_K1 = len(dec_K2_div_K1) / len(K1)
    p_dec_K1 = len(dec_K1) / n
    p_dec_K2 = len(dec_K2) / n

    error_probability = (len(dec_K1_div_K2) + len(dec_K2_div_K1)) / n
    correct_decision_probability = 1 - error_probability

    # building table
    col_names = ["№", "Вираз", "Значення", "№", "Вираз", "Значення"]
    table_data = [
        ["1", "n(ріш К1 / K1)", len(dec_K1_div_K1), "2", "n(ріш К2 / K2)", len(dec_K2_div_K2)],
        ["3", "n(ріш К1 / K2)", len(dec_K1_div_K2), "4", "n(ріш К2 / K1)", len(dec_K2_div_K1)],
        ["5", "n(ріш K1)", len(dec_K1), "6", "n(ріш К2)", len(dec_K2)],
        ["7", "P(K2 | ріш K1)", p_K2_div_dec_K1, "8", "P(K1 | ріш K2)", p_K1_div_dec_K2],
        ["9", "P(ріш K1 | K2)", p_dec_K1_div_K2, "10", "P(ріш K2 | K1)", p_dec_K2_div_K1],
        ["11", "P(ріш К1)", p_dec_K1, "12", "P(ріш К2)", p_dec_K2],
        ["13", "P(помилки)", error_probability, "14", "P(вірних ріш.)", correct_decision_probability],
    ]

    print(tabulate(table_data, headers=col_names, tablefmt="fancy_grid"))

    print("Граничне значення U:", x_threshold_value)
    print("Граничне значення a:", y_threshold_value)

    # showing the correlation field
    plt.plot(dec_K1_div_K1['U'], dec_K1_div_K1['a'], 'go', label='ріш К1 / К1')
    plt.plot(dec_K1_div_K2['U'], dec_K1_div_K2['a'], 'ro', label='ріш К1 / К2')
    plt.plot(dec_K2_div_K2['U'], dec_K2_div_K2['a'], 'bo', label='ріш К2 / К2')
    plt.plot(dec_K2_div_K1['U'], dec_K2_div_K1['a'], 'yo', label='ріш К2 / К1')

    plt.plot(np.full(2, x_threshold_value), [0, y_max])
    plt.plot([0, x_max], np.full(2, y_threshold_value))

    plt.title("Поле кореляції")
    plt.legend()

    plt.show()


if __name__ == '__main__':
    main()
