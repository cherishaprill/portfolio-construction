import pandas as pd

prices = pd.DataFrame({"BLUE": [8.70, 8.91, 8.71, 8.43, 8.73], "ORANGE": [10.66, 11.08, 10.71, 11.59, 12.11]})
prices

prices.iloc[1:]
prices.iloc[:-1]
returns = prices.iloc[1:].values/prices.iloc[:-1] - 1
returns