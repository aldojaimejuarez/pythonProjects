"""
Created on Aug 2021

@author: me@aldojaimejuarez.com

coding: utf-8

version : 1.1

Description: 
Create a price analysis of 2 differents oil types (Brent and WTI), 
calculate the moving average of the last 7 days, 
get the analysis from the year 2000 until the most recent available data in the CSVs,
get a similar output of the example (image)

"""

def main():

    
    import pandas as pd 

    #BRENT
    brent_daily = pd.read_csv('brent-daily.csv', header=0) #Read initial file
    brent_daily['Price_Average'] = brent_daily['Price'].rolling(7).mean() #Add Price_Average column: moving average last 7 days 
    add_column = brent_daily.assign(Oil_Type='Brent') #Add Oil_Type column
    filtered_date = add_column[add_column['Date']> '2000-01-01'] #Filtered by date
    delete_price_column = filtered_date.iloc[:, [0,2,3]] #Delete price column
    frame=delete_price_column #Creating frame variable
    #print(frame) #Check Brent frame


    #WTI
    wti_daily = pd.read_csv('wti-daily.csv', header=0) #Read initial file
    wti_daily['Price_Average'] = wti_daily['Price'].rolling(7).mean() #Add Price_Average column: moving average last 7 days 
    add_column2 = wti_daily.assign(Oil_Type='WTI') #Add Oil_Type column
    filtered_date2 = add_column2[add_column2['Date']> '2000-01-01'] #Filtered by date
    delete_price_column2 = filtered_date2.iloc[:, [0,2,3]] #Delete price column
    frame2=delete_price_column2 #Creating frame2 variable
    #print(frame2) #Check WTI frame


    #CONCAT
    frames = [frame, frame2] #Listing data frames
    concat_frames = pd.concat(frames) #Concating data frames
    order_by = concat_frames.sort_values(by=['Date', 'Oil_Type']) #Order by Date and Oil_Type
    output = order_by #Creating output variable
    #print(output) #Check final output
    output.to_csv('output.csv', encoding='utf-8', index=False) #Creating the output file 


if __name__ == '__main__':
    main()
