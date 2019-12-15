#IMPORT PACKAGES NEEDED

import yahoofinance as yf #https://pypi.org/project/yahoo-finance/#
import pandas_datareader as pdr #https://pandas.pydata.org/pandas-docs/stable/install.html
import datetime #https://docs.python.org/3/library/datetime.html
import sys #https://docs.python.org/3/library/sys.html
import os ##https://docs.python.org/2/library/os.html?highlight=os#module-os
import pathlib #https://docs.python.org/3/library/pathlib.html

#ALL DATA WAS TAKEN FROM YAHOO FINANCE USING THE YAHOO FINANCE PACKAGE AVAILABLE VIA PYTHON

#THIS FILE PULLS STOCKS HISTORICAL PRICE FOR ANY DATE RANGE VIA USER INPUT, 
#SAVES IT TO A FOLDER CREATED VIA USER INPUT AND NAMES IT VIA USER INPUT.

#get stock information function
def create_file_get_stock():
    
    while 1:
        
        try:
            #Create Directory
            create_directory = input("=> Would you like create and save this stock information to a new Directory located on your Desktop? [Y]/[N]:  ")
            
            if create_directory == "Y":
                
                new_directory = input("=> Enter new directory name:  ")
                
                os.mkdir(new_directory)
                
                try:
                    #Input date range, ticker symbol, saves to directory
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
                        #If file already exists, asks user to enter a different file name
                        print("=> File name already exists, please choose a different name...\n")
                        
                    else:
                        #If file does not exist, file will be created
                        print("=> File does not exist, creating file...\n")

                #keyboard interrupt to end script        
                except KeyboardInterrupt:
                    
                    print("\n=> Keyboard Interrupt! Exiting Program...\n")
                    sys.exit()

            #If user does not want to create new directory to save csv file
            elif create_directory == "N":

                #user input to which folder to be saved
                new_directory = input("=> Enter directory name to save file:  ")
                print("=> No new directory created, saving file to folder " + new_directory)

                try:
                    #Input date range, ticker symbol, saves to directory
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
                        #If file already exists, asks user to enter a different file name
                        print("=> File name already exists, please choose a different name...\n")
                        
                    else:
                        #If file does not exist, file will be created
                        print("=> File does not exist, creating file...\n")

                #keyboard interrupt to end script        
                except KeyboardInterrupt:
                    
                    print("\n=> Keyboard Interrupt! Exiting Program...\n")
                    sys.exit()

            #check if input is valid, if not asks user to enter a valid input and reruns the loop
            elif create_directory != "Y" or create_directory != "N":
                print("=> Please enter valid response... [Y]/[N]\n")
                
            else:
                return True
            
        except OSError as e:

            print("=> Directory already exists... no new directory created\n")

#call function      
create_file_get_stock()



