"""
Created on Tue Sep 28 2021
@author: me@aldojaimejuarez.com
coding: utf-8
"""

import pandas as pd 

brentDaily = pd.read_csv('brent-daily.csv', header=0)
wtiDaily = pd.read_csv('wti-daily.csv', header=0)


#BRENT
filter_date = brentDaily[brentDaily['Date']> '1999-12-13']
filter_date['moving_average_7days'] = filter_date['Price'].rolling(7).mean()
moving_average_7days = filter_date
moving_average_7days.columns = ['Date','Price', 'Price_Average']
date_and_price_average = moving_average_7days.iloc[:, [0,2]]
output1 = date_and_price_average.assign(Oil_Type='Brent')
#print(output1)
#output1.to_csv('output1.csv', encoding='utf-8', index=False)


#WTI
filter_date2 = wtiDaily[wtiDaily['Date']> '1999-12-13']
filter_date2['moving_average_7days'] = filter_date2['Price'].rolling(7).mean()
moving_average_7days2 = filter_date2
moving_average_7days2.columns = ['Date','Price', 'Price_Average']
date_and_price_average2 = moving_average_7days2.iloc[:, [0,2]]
output2 = date_and_price_average2.assign(Oil_Type='WTI')
#print(output2)
#output2.to_csv('output2.csv', encoding='utf-8', index=False)


#CONCAT
output3 = pd.concat([output1, output2])
output4 = output3.sort_values(by=['Date', 'Oil_Type'])
#print(output4)
output5 = output4[output4['Date']> '2000-01-01']
#print(output5)
output5.to_csv('output5.csv', encoding='utf-8', index=False)