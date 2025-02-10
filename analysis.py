"""
求出金叉、死叉制定双均线策略
"""
from unittest.mock import inplace

import numpy as np
import pandas as pd
from pandas import DataFrame, Series

df = pd.read_csv('./000001.SZ.csv')
df['trade_date'] = pd.to_datetime(df['trade_date'])
df.set_index('trade_date', inplace=True)

# 挑选出开盘比前一日收盘跌幅超过2%的日期（没什么用处写着玩）
# bol = (df['open'] - df['open'].shift(1)) / df['open'].shift(1) < -0.02

# 双均线(5日均线与30日均线)
ma5 = df['close'].rolling(5).mean()[30:]
ma30 = df['close'].rolling(30).mean()[30:]
df = df[30:]
s1 = ma5 < ma30
s2 = ma5 > ma30

# 获取金叉和死叉日期
golden_date = df.loc[~(s1 | s2.shift(1))].index
death_date = df.loc[s1 & s2.shift(1)].index


# 初始资金为10000元，金叉尽量买入，死叉尽量卖出，到2025年1月1日的炒股收益
f1 = Series(data=1, index=golden_date)  # 金叉标识
f2 = Series(data=0, index=death_date)  # 死叉标识
s = pd.concat([f1, f2]).sort_index()
cost = 10000
money = cost
hold = 0  # 拥有的股票手数(一手100股)

for i in range(len(s)):
    time = s.index[i]
    p = df.loc[time, 'open']
    if i == 1:
        hold, money = divmod(money, p*100)
    else:
        money += 100 * hold * p
        hold = 0
profit = money + 100 * hold * df['close'][-1]
print(profit)






