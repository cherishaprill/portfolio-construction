import pandas as pd

prices = pd.DataFrame({"BLUE": [8.70, 8.91, 8.71, 8.43, 8.73], "ORANGE": [10.66, 11.08, 10.71, 11.59, 12.11]})
prices

prices.iloc[1:]
prices.iloc[:-1]
returns = prices.iloc[1:].values/prices.iloc[:-1] - 1
returns

### read csv file 
me_m=pd.read_csv("Desktop/portfolio_python/data/Portfolios_Formed_on_ME_monthly_EW.csv", 
                 header=0, index_col=0, parse_dates=True, na_values=-99.99)
rets=me_m[['Lo 10', 'Hi 10']]
rets.columns = ['SmallCap', 'LargeCap']
rets = rets/100
rets.plot.line()
