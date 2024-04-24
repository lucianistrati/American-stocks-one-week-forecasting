import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


class StockDataPreprocessor:
    def __init__(self, data_folder="data", output_folder="stocks"):
        self.data_folder = data_folder
        self.output_folder = output_folder
        self.tickers = ["GS", "C", "WFC", "BAC", "JPM"]
        self.relevant_cols = ["Open", "High", "Low", "Close", "Volume"]

    def preprocess_data(self):
        os.makedirs(self.output_folder, exist_ok=True)
        for ticker in self.tickers:
            df = pd.read_excel(os.path.join(self.data_folder, "DataSet_Target Portfolio.xlsx"), sheet_name=ticker)
            closes = df["Close"].to_list()
            adj_closes = df["Adj Close"].to_list()
            price_diffs = [c - ac for (c, ac) in zip(closes, adj_closes)]
            df = df[self.relevant_cols]
            df.to_csv(os.path.join(self.output_folder, f"{ticker}_tick_data.csv"))
            self.plot_price_diff(ticker, price_diffs)

    def plot_price_diff(self, ticker, price_diffs):
        plt.plot(price_diffs)
        plt.title(f"{ticker} Price Difference")
        plt.xlabel("Days")
        plt.ylabel("Price Difference")
        plt.savefig(os.path.join(self.output_folder, f"{ticker}_price_difference.png"))
        plt.show()

# GS, C, WFC, BAC, JPM
tickers = ["GS", "C", "WFC", "BAC", "JPM"]
cols = ["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]
relevant_cols = ["Open", "High", "Low", "Close", "Volume"]

plot = True

os.system("stocks")

if __name__ == "__main__":
    preprocessor = StockDataPreprocessor()
    preprocessor.preprocess_data()

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
            
