import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# GS, C, WFC, BAC, JPM
tickers = ["GS", "C", "WFC", "BAC", "JPM"]
cols = ["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]
relevant_cols = ["Open", "High", "Low", "Close", "Volume"]

plot = True

os.system("stocks")

for ticker in tickers:
    df = pd.read_excel("data/DataSet_Target Portfolio.xlsx", sheet_name=ticker)#, engine='openpyxl')

    closes = df["Close"].to_list()
    adj_closes = df["Adj Close"].to_list()

    print(closes == adj_closes)

    closes = [c - ac for (c, ac) in zip(closes, adj_closes)]

    df = df[relevant_cols]
    print(type(df))
    df.to_csv(f"stocks/{ticker}_tick_data.csv")

    if plot:
        plt.plot(closes)
        plt.title(ticker)
        plt.show()



