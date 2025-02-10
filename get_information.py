"""
使用Tushare包获取某股票的历史行情数据，并保存到本地
"""


import pandas as pd
import tushare as ts

# 设置token和初始化pro接口
ts.set_token('a835a58976d05685d817491447964a0f9af37704d88f2b5c37b3af80')
pro = ts.pro_api()

# 获取数据并进行处理
df = pro.daily(ts_code='000001.SZ', start_date='20240101', end_date='20250101')
df['trade_date'] = pd.to_datetime(df['trade_date'])
df.set_index('trade_date', inplace=True)
print(df.info())
#df.to_csv('./000001.SZ.csv')
