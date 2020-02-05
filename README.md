# University Of Colorado Boulder Fall 2019 Structured Data project
## Contributors:
* Wenbin Yang GitHub: wenbin-yang
* Alyson Chen GitHub: alysonchen
* Alex Qaddourah GitHub: alexqaddourah
## Overiew
* This project consisted of building a relational database using MySQL Workbench. The data used was stock data pulled from Yahoo Finance using the yahoo-finance Python library. The data base was built using mysql-connector-python Python library. All code is included in this repo and is reproducible but requires the following: Python and MySQL Workbench.
## File breakdown
*** The CSV files in the repo can be used to recreate the project. When running the code make sure to change the file location
you want to save it to. These will be inputs since the code also uses the OS python library.
1. companyinfo.py - used to compile company information for any publicaly traded company which Yahoo Finance has data on.
..* Note - csv files were edited to the orrect format once all profiles were pulled
``` python
#import libaries needed
import yahoofinance as yf #https://pypi.org/project/yahoo-finance/#
import sys #https://docs.python.org/3/library/sys.html

#company profile detail
def get_profile():
    while 1:
        try:
            symbol = input("=> Enter Stock Symbol: ")
            profile = yf.AssetProfile(symbol)
            symbol_1 = symbol+"-profile.csv"
            profile.to_csv(symbol_1)
        except KeyboardInterrupt:
            print("\n=> Keyboard Interrupt! Exiting Program...")
            sys.exit()
get_profile()
     
#csv files were edited to correct format once all profiles were pulled
#this script was use to get company_execs and all_profiles
```
2. stockpricev2.py - used to pull the stock price information for any publicaly traded company which Yahoo Finance has data on.
``` python
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
```   
3. mysqlprojectv3.py - script used to create/ connect to MySQL Workbench (database was locally hosted).
``` python
#import packages
import mysql.connector #https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
import getpass #https://docs.python.org/2/library/getpass.html
import os #https://docs.python.org/2/library/os.html?highlight=os#module-os
import csv #https://docs.python.org/2/library/csv.html

#mycursor
#execute
#executemany (all)

mydb = mysql.connector.connect(
    host=input("Enter host: "),
    user=input("Enter user: "),
    passwd=getpass.getpass("Enter Password for db: "),
    auth_plugin="mysql_native_password"
)

#establish mycursor variable
mycursor = mydb.cursor()
#drop schema if exists
mycursor.execute("DROP SCHEMA IF EXISTS Avengers")
#creates database
mycursor.execute("CREATE DATABASE IF NOT EXISTS Avengers")
#select db to use
mycursor.execute("USE Avengers")
#show list of db once created
mycursor.execute("SHOW DATABASES")
#print databases to console
for x in mycursor:
    print(x)

#create company profile table
mycursor.execute("DROP TABLE IF EXISTS all_profiles")
mycursor.execute("CREATE TABLE IF NOT EXISTS all_profiles (CompanyCode VARCHAR(5),\
    Addres VARCHAR(30),\
    City VARCHAR(15),\
    State VARCHAR(2),\
    Country VARCHAR(15),\
    PhoneNumber VARCHAR(16),\
    Website VARCHAR(30),\
    Sector VARCHAR(30),\
    Industry VARCHAR(50),\
    Employees INT,\
    primary key (CompanyCode))")

#create executives table
mycursor.execute("DROP TABLE IF EXISTS company_execs")
mycursor.execute("CREATE TABLE IF NOT EXISTS company_execs (CompanyCode VARCHAR(5),\
    Name VARCHAR(45),\
    Title VARCHAR(100),\
    Pay INT NULL,\
    Exercised INT NULL,\
    YearBorn VARCHAR(4),\
    foreign key(CompanyCode) references CompanyProfiles(CompanyCode))")

#create all the stock tables
mycursor.execute("DROP TABLE IF EXISTS aaplstockprice")
mycursor.execute("CREATE TABLE IF NOT EXISTS aaplstockprice (CompanyCode VARCHAR(5),\
    date DATE NOT NULL,\
    high DECIMAL(7,3),\
    low DECIMAL(7,3),\
    open DECIMAL(7,3),\
    close DECIMAL(7,3),\
    volume INT,\
    adjClose DECIMAL(7,3),\
    foreign key(CompanyCode) references CompanyProfiles(CompanyCode))")

mycursor.execute("DROP TABLE IF EXISTS amznstockprice")
mycursor.execute("CREATE TABLE IF NOT EXISTS amznstockprice (CompanyCode VARCHAR(5),\
    date DATE NOT NULL,\
    high DECIMAL(7,3),\
    low DECIMAL(7,3),\
    open DECIMAL(7,3),\
    close DECIMAL(7,3),\
    volume INT,\
    adjClose DECIMAL(7,3),\
    foreign key(CompanyCode) references CompanyProfiles(CompanyCode))")

mycursor.execute("DROP TABLE IF EXISTS fbstockprice")
mycursor.execute("CREATE TABLE IF NOT EXISTS fbstockprice (CompanyCode VARCHAR(5),\
    date DATE NOT NULL,\
    high DECIMAL(7,3),\
    low DECIMAL(7,3),\
    open DECIMAL(7,3),\
    close DECIMAL(7,3),\
    volume INT,\
    adjClose DECIMAL(7,3),\
    foreign key(CompanyCode) references CompanyProfiles(CompanyCode))")

mycursor.execute("DROP TABLE IF EXISTS googlestockprice")
mycursor.execute("CREATE TABLE IF NOT EXISTS googlestockprice (CompanyCode VARCHAR(5),\
    date DATE NOT NULL,\
    high DECIMAL(7,3),\
    low DECIMAL(7,3),\
    open DECIMAL(7,3),\
    close DECIMAL(7,3),\
    volume INT,\
    adjClose DECIMAL(7,3),\
    foreign key(CompanyCode) references CompanyProfiles(CompanyCode))")

mycursor.execute("DROP TABLE IF EXISTS ibmstockprice")
mycursor.execute("CREATE TABLE IF NOT EXISTS ibmstockprice (CompanyCode VARCHAR(5),\
    date DATE NOT NULL,\
    high DECIMAL(7,3),\
    low DECIMAL(7,3),\
    open DECIMAL(7,3),\
    close DECIMAL(7,3),\
    volume INT,\
    adjClose DECIMAL(7,3),\
    foreign key(CompanyCode) references CompanyProfiles(CompanyCode))")

mycursor.execute("DROP TABLE IF EXISTS intcstockprice")
mycursor.execute("CREATE TABLE IF NOT EXISTS aaplstockprice (CompanyCode VARCHAR(5),\
    date DATE NOT NULL,\
    high DECIMAL(7,3),\
    low DECIMAL(7,3),\
    open DECIMAL(7,3),\
    close DECIMAL(7,3),\
    volume INT,\
    adjClose DECIMAL(7,3),\
    foreign key(CompanyCode) references CompanyProfiles(CompanyCode))")

mycursor.execute("DROP TABLE IF EXISTS msftstockprice")
mycursor.execute("CREATE TABLE IF NOT EXISTS msftstockprice (CompanyCode VARCHAR(5),\
    date DATE NOT NULL,\
    high DECIMAL(7,3),\
    low DECIMAL(7,3),\
    open DECIMAL(7,3),\
    close DECIMAL(7,3),\
    volume INT,\
    adjClose DECIMAL(7,3),\
    foreign key(CompanyCode) references CompanyProfiles(CompanyCode))")

mycursor.execute("DROP TABLE IF EXISTS oraclestockprice")
mycursor.execute("CREATE TABLE IF NOT EXISTS oraclestockprice (CompanyCode VARCHAR(5),\
    date DATE NOT NULL,\
    high DECIMAL(7,3),\
    low DECIMAL(7,3),\
    open DECIMAL(7,3),\
    close DECIMAL(7,3),\
    volume INT,\
    adjClose DECIMAL(7,3),\
    foreign key(CompanyCode) references CompanyProfiles(CompanyCode))")

mycursor.execute("DROP TABLE IF EXISTS techystockprice")
mycursor.execute("CREATE TABLE IF NOT EXISTS techystockprice (CompanyCode VARCHAR(5),\
    date DATE NOT NULL,\
    high DECIMAL(7,3),\
    low DECIMAL(7,3),\
    open DECIMAL(7,3),\
    close DECIMAL(7,3),\
    volume INT,\
    adjClose DECIMAL(7,3),\
    foreign key(CompanyCode) references CompanyProfiles(CompanyCode))")

#show tables
mycursor.execute("SHOW TABLES")
#print tables created to console
for x in mycursor:
    print(x)

#read, import csv file to sql db
with open('all_profiles.csv', 'r') as csvfile:
    csvReader = csv.reader(csvfile)
    next(csvReader)
    for row in csvReader:
        try:
            mycursor.execute("INSERT INTO all_profiles (\
                CompanyCode,\
                Addres,\
                City,\
                State,\
                Country,\
                PhoneNumber,\
                Website,\
                Sector,\
                Industry,\
                Employees) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            tuple(row))
            mydb.commit()
        except Exception as e:
            break
            print(e)
print("Data imported into all_profiles table\n")

#read, import csv file to sql db
with open('company_execs.csv', 'r') as csvfile:
    csvReader = csv.reader(csvfile)
    next(csvReader)
    for row in csvReader:
        try:
            mycursor.execute("INSERT INTO company_execs (\
                Name,\
                Title,\
                Pay,\
                Exercised,\
                YearBorn,\
                CompanyCode) VALUES (%s, %s, %s, %s, %s, %s)",
            tuple(row))
            mydb.commit()
        except Exception as e:
            break
            print(e)
print("Data imported into company_execs table\n")

#read, import csv file to sql db
with open('aapl.csv', 'r') as csvfile:
    csvReader = csv.reader(csvfile)
    next(csvReader)
    for row in csvReader:
        try:
            mycursor.execute("INSERT INTO aaplstockprice (\
                date,\
                high,\
                low,\
                open,\
                close,\
                volume,\
                adjClose,\
                code)) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            tuple(row))
            mydb.commit()
        except Exception as e:
            break
            print(e)
print("Data imported into aaplstockprice table\n")

#read, import csv file to sql db
with open('amzn.csv', 'r') as csvfile:
    csvReader = csv.reader(csvfile)
    next(csvReader)
    for row in csvReader:
        try:
            mycursor.execute("INSERT INTO amznstockprice (\
                date,\
                high,\
                low,\
                open,\
                close,\
                volume,\
                adjClose,\
                code)) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            tuple(row))
            mydb.commit()
        except Exception as e:
            break
            print(e)
print("Data imported into amznstockprice table\n")

#read, import csv file to sql db
with open('fb.csv', 'r') as csvfile:
    csvReader = csv.reader(csvfile)
    next(csvReader)
    for row in csvReader:
        try:
            mycursor.execute("INSERT INTO fbstockprice (\
                date,\
                high,\
                low,\
                open,\
                close,\
                volume,\
                adjClose,\
                code)) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            tuple(row))
            mydb.commit()
        except Exception as e:
            break
            print(e)
print("Data imported into fbstockprice table\n")

#read, import csv file to sql db
with open('goog.csv', 'r') as csvfile:
    csvReader = csv.reader(csvfile)
    next(csvReader)
    for row in csvReader:
        try:
            mycursor.execute("INSERT INTO googlestockprice (\
                date,\
                high,\
                low,\
                open,\
                close,\
                volume,\
                adjClose,\
                code)) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            tuple(row))
            mydb.commit()
        except Exception as e:
            break
            print(e)
print("Data imported into googlestockprice table\n")

#read, import csv file to sql db
with open('ibm.csv', 'r') as csvfile:
    csvReader = csv.reader(csvfile)
    next(csvReader)
    for row in csvReader:
        try:
            mycursor.execute("INSERT INTO ibmstockprice (\
                date,\
                high,\
                low,\
                open,\
                close,\
                volume,\
                adjClose,\
                code)) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            tuple(row))
            mydb.commit()
        except Exception as e:
            break
            print(e)
print("Data imported into ibmstockprice table\n")

#read, import csv file to sql db
with open('intc.csv', 'r') as csvfile:
    csvReader = csv.reader(csvfile)
    next(csvReader)
    for row in csvReader:
        try:
            mycursor.execute("INSERT INTO intcstockprice (\
                date,\
                high,\
                low,\
                open,\
                close,\
                volume,\
                adjClose,\
                code)) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            tuple(row))
            mydb.commit()
        except Exception as e:
            break
            print(e)
print("Data imported into intcstockprice table\n")

#read, import csv file to sql db
with open('msft.csv', 'r') as csvfile:
    csvReader = csv.reader(csvfile)
    next(csvReader)
    for row in csvReader:
        try:
            mycursor.execute("INSERT INTO msftstockprice (\
                date,\
                high,\
                low,\
                open,\
                close,\
                volume,\
                adjClose,\
                code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            tuple(row))
            mydb.commit()
        except Exception as e:
            break
            print(e)
print("Data imported into msftstockprice table\n")

#read, import csv file to sql db
with open('orcl.csv', 'r') as csvfile:
    csvReader = csv.reader(csvfile)
    next(csvReader)
    for row in csvReader:
        try:
            mycursor.execute("INSERT INTO oraclestockprice (\
                 date,\
                high,\
                low,\
                open,\
                close,\
                volume,\
                adjClose,\
                code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            tuple(row))
            mydb.commit()
        except Exception as e:
            break
            print(e)
print("Data imported into oraclestockprice table\n")

#read, import csv file to sql db
with open('techy.csv', 'r') as csvfile:
    csvReader = csv.reader(csvfile)
    next(csvReader)
    for row in csvReader:
        try:
            mycursor.execute("INSERT INTO techystockprice (\
                date,\
                high,\
                low,\
                open,\
                close,\
                volume,\
                adjClose,\
                code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            tuple(row))
            mydb.commit()
        except Exception as e:
            break
            print(e)
print("Data imported into techystockprice table\n")

mycursor.close()
mydb.commit()
mydb.close()
```
