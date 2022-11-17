import matplotlib as plt
import pandas as pd


def load_csv(filename: str) -> pd.DataFrame:
    return pd.read_csv(filename)


def main():
    filename = "data.csv"
    df = load_csv(filename)
    print(df)


if __name__ == '__main__':
    main()


