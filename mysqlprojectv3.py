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
