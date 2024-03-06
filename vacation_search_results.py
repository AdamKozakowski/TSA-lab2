import numpy as np
import pandas as pd
import csv

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