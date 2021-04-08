import pandas as pd
import matplotlib.pyplot as plt
import os


def symbol_to_path(symbol, base_dir="data"):
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    df = pd.DataFrame(index=dates)
    for symbol in symbols:
        path = symbol_to_path(symbol)
        df_temp = pd.read_csv(path,
                              index_col="Date",
                              parse_dates=True,
                              na_values=["nan"],
                              converters={'Volume': lambda x: float(x.replace(',', '').replace(',', '.'))},
                              usecols=["Date", "Volume"])
        df_temp = df_temp.rename(columns={"Volume": symbol})
        df = df.join(df_temp)

    df = df.dropna()
    return df


def draw_chart():
    symbols = ["AAPL", "GOOG"]

    start_date = '2021-01-01'
    end_date = '2021-07-04'
    dates = pd.date_range(start_date, end_date)

    df = get_data(symbols, dates)

    print df.head()
    df.plot()
    plt.show()


if __name__ == "__main__":
    draw_chart()
