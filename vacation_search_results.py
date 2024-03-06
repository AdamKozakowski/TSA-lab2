import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt

#Import csv files.
vacation_PL_df= pd.read_csv('vacationPL.csv')

#Set datetime index for each dataframe
vacation_PL_df.set_index('datatime',inplace=True)
vacation_UK_df= pd.read_csv('vacationUK.csv', index_col='datatime')
vacation_USA_df= pd.read_csv('vacationUSA.csv', index_col='datatime')

#rename columns using country codes (eg. PL) as headers.
vacation_PL_df = vacation_PL_df.rename(columns={'vacation': 'vacation_PL'})
vacation_UK_df = vacation_UK_df.rename(columns={'vacation': 'vacation_UK'})
vacation_USA_df = vacation_USA_df.rename(columns={'vacation': 'vacation_USA'})

# Combine the search counts in one dataframe.
vacation_combined_df = pd.concat([vacation_PL_df, vacation_UK_df, vacation_USA_df], axis=1)
# vacation_combined_df.info()
# print(vacation_combined_df.head())
#output: 
#           vacation_PL  vacation_UK  vacation_USA
# datatime
# 2004-01             0           41            98
# 2004-02           100           38            88
# 2004-03             0           43            81
# 2004-04             0           36            78

#present the time series for all countries in one plot
# Plot the time series data for all countries in one plot
# plt.figure(figsize=(20, 6)) 
# plt.plot(vacation_combined_df.index, vacation_combined_df['vacation_PL'], label='Poland')
# plt.plot(vacation_combined_df.index, vacation_combined_df['vacation_UK'], label='United Kingdom')
# plt.plot(vacation_combined_df.index, vacation_combined_df['vacation_USA'], label='United States')
# plt.xlabel('Date')
# plt.xticks(vacation_combined_df.index[::12], rotation=45) 
# plt.ylabel('Vacation')
# plt.title('Vacation Time Series for PL, UK and USA')
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.show()

# Generate descriptive statistics
print(vacation_combined_df.describe())

