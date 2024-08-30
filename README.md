# American Stocks One-Week Forecasting

## Overview

This project aims to preprocess historical stock data of American financial institutions and visualize the price differences between the 'Close' and 'Adj Close' prices. Additionally, it provides functionality to save the preprocessed data and plots for further analysis.

## Code

The repository contains the following files:

- **main.py**: Python script for preprocessing the historical stock data and plotting the price differences.
- **data**: Folder containing the raw dataset ('DataSet_Target Portfolio.xlsx').
- **stocks**: Folder where the preprocessed data and plots will be saved.
  
### Preprocessing Steps:

1. Load the raw dataset from 'DataSet_Target Portfolio.xlsx' for each stock ticker.
2. Calculate the price differences between the 'Close' and 'Adj Close' prices.
3. Extract relevant columns ('Open', 'High', 'Low', 'Close', 'Volume') for further analysis.
4. Save the preprocessed data in CSV format in the 'stocks' folder.
5. Plot and save the price differences for visualization.

## Usage

To preprocess the stock data and visualize price differences, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/American-stocks-one-week-forecasting.git
   ```
2. Navigate to the project directory:
   ```bash
   cd American-stocks-one-week-forecasting
   ```
3. Ensure the raw dataset ('DataSet_Target Portfolio.xlsx') is in the 'data' folder.
4. Run the main script:
   ```bash
   python main.py
   ```

## Results

The preprocessed data and plots are saved in the 'stocks' folder. You can analyze the price differences between the 'Close' and 'Adj Close' prices for each stock ticker.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or create a pull request.
