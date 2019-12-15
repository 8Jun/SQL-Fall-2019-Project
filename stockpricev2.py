#get historical
import yahoofinance as yf
import pandas_datareader as pdr
import datetime
import sys
import os
import pathlib


#get stock price information for whatever date range needed
#saves to a csv file

def create_file_get_stock():
    
    while 1:
        
        try:
            
            create_directory = input("=> Would you like create and save this stock information to a new Directory located on your Desktop? [Y]/[N]:  ")
            
            if create_directory == "Y":
                
                new_directory = input("=> Enter new directory name:  ")
                
                os.mkdir(new_directory)
                
                try:
                    
                    symbol = input("=> Enter Stock Symbol (lower case):  ")
                    start = input("=> Enter Start Date in YYYY-MM-DD format:  ")
                    end = input("=> Enter End Date in YYYY-MM-DD format:  ")
                    start_year, start_month, start_day = map(int, start.split("-"))
                    end_year, end_month, end_day = map(int, end.split("-"))
                    start_date = datetime.datetime(start_year, start_month, start_day)
                    end_date = datetime.datetime(end_year, end_month, end_day)
                    df = pdr.DataReader(symbol, "yahoo", start_date, end_date)
                    stock_file = df.to_csv(os.path.join(new_directory,input("=> Enter File Name to be saved with .csv at the end:  ")))
                    path = pathlib.Path(str(stock_file))
                    
                    if path.exists():
                        
                        print("=> File name already exists, please choose a different name...\n")
                        
                    else:
                        
                        print("=> File does not exist, creating file...\n")
                        
                except KeyboardInterrupt:
                    
                    print("\n=> Keyboard Interrupt! Exiting Program...\n")
                    sys.exit()

            elif create_directory == "N":
                
                new_directory = input("=> Enter directory name to save file:  ")
                print("=> No new directory created, saving file to folder " + new_directory)
                
                try:
                    
                    symbol = input("=> Enter Stock Symbol (lower case):  ")
                    start = input("=> Enter Start Date in YYYY-MM-DD format:  ")
                    end = input("=> Enter End Date in YYYY-MM-DD format:  ")
                    start_year, start_month, start_day = map(int, start.split("-"))
                    end_year, end_month, end_day = map(int, end.split("-"))
                    start_date = datetime.datetime(start_year, start_month, start_day)
                    end_date = datetime.datetime(end_year, end_month, end_day)
                    df = pdr.DataReader(symbol, "yahoo", start_date, end_date)
                    stock_file = df.to_csv(os.path.join(new_directory,input("=> Enter File Name to be saved with .csv at the end:  ")))
                    path = pathlib.Path(str(stock_file))
                    
                    if path.exists():
                        
                        print("=> File name already exists, please choose a different name...\n")
                        
                    else:
                        
                        print("=> File does not exist, creating file...\n")
                        
                except KeyboardInterrupt:
                    
                    print("\n=> Keyboard Interrupt! Exiting Program...\n")
                    sys.exit()

            elif create_directory != "Y" or create_directory != "N":
                print("=> Please enter valid response... [Y]/[N]\n")
                
            else:
                return True
            
        except OSError as e:
            
            print("=> Directory already exists... no new directory created\n")
        
create_file_get_stock()



