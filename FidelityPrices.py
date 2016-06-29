import os 
import subprocess
import urllib.request
import csv 
import pandas as pd
from pandas import Series, DataFrame
from pandas import ExcelWriter 
from pandas import read_csv 

def GetPrices():
    """ Goes to the URL, Reads the CSV download link, and creates the CSV DataFrame"""
    url = "http://fundresearch.fidelity.com/mutual-funds/fidelity-funds-daily-pricing-yields/download"
    CSV_Import = urllib.request.urlopen(url).read() 
    CSV = pd.read_csv(url, skiprows=3) 
    
    """ Creates CSV File to be opened in Excel. 
    This can be removed if you don't need Excel and you can just use CSV as the DataFrame """ 
    File = 'DailyPrices'
    writer = ExcelWriter(str(File) + '.xlsx')
    CSV.to_excel(writer, 'DailyReport', index = False)
    writer.close() 
    os.startfile(File + '.xlsx') 
    
GetPrices() 
