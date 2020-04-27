# University Of Colorado Boulder Fall 2019 Structured Data project

## Executive Summary:
This project was designed to give our team a hands on approach to mySQL, and explore what more we could do with it. We had an interest into stock prices around this time, and thought that since stocks are neatly arranged in fields, we could build a database that would help us retrieve stock information. A key component of this project was using the SQL-Python connector to build and code the SQL database inside Python, and then run quieries in SQL language to answer self-created business questions.

Our team first built the Python code (all code below) that imports the desired stock from Yahoo finance. It loads all of the requested stock codes into a directory. Then, we use the connector to build our database with table names and parameters. We then loaded all of the files in.

Our report shows basic to more advanced SQL commands (from SELECT to JOIN to Subqueries) and answers several self-created business questions we believe top level managers might ask a business analyst. 

Main takeaways from this project:
* This project helped our team hone our skills with SQL language and explore what more can be connected to SQL. After this project, all of us have very good understanding of the SQL language and feel confident both building and navigating through a database, no matter the size. 

## Contributors:

* Wenbin Yang GitHub: wenbin-yang
* Alyson Chen GitHub: alysonchen
* Alex Qaddourah GitHub: alexqaddourah
* Junji Wiener GitHub: 8Jun

### Overiew:

* This project consisted of building a relational database using MySQL Workbench. The data used was stock data pulled from Yahoo Finance using the yahoo-finance Python library. The data base was built using mysql-connector-python Python library. All code is included in this repo and is reproducible but requires the following: Python and MySQL Workbench.

### File breakdown:

*** The CSV files in the repo can be used to recreate the project. When running the code make sure to change the file location
you want to save it to. These will be inputs since the code also uses the OS python library.
1. companyinfo.py - used to compile company information for any publicaly traded company which Yahoo Finance has data on.
..* Note - csv files were edited to the orrect format once all profiles were pulled

## Code Preview:

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
```

4. Create tables

``` python
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

mycursor.close()
mydb.commit()
mydb.close()
```
## ER Model:

![alt text](https://github.com/8Jun/SQL-Fall-2019-Project/blob/master/ER%20Model.PNG)
