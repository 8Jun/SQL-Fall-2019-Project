drop database if exists _weya9345_project;
create database _weya9345_project;
use _weya9345_project;


Drop table if exists all_profiles;
create table if not exists all_profiles(
    `CompanyCode` Varchar(100) not null,
	`Address` Varchar(100) not null,
	`City` Varchar(100) not null,
    `State` Varchar(100),
    `Country` Varchar(100) not null,
    `Phone` Varchar(100) not null,
    `Website` Varchar(100) not null,
    `Sector` Varchar(100) not null,
    `Industry` Varchar(100) not null,
    `Employees` int not null,
    PRIMARY KEY (`CompanyCode`));

Drop table if exists company_execs;
create table if not exists company_execs(
    `Name` Varchar(100) not null,
	`Title` Varchar(100) not null,
	`Pay` Varchar(100),
    `Exercised` Varchar(100),
    `Year Born` Varchar(100),
    `CompanyCode` Varchar(100) not null,
    PRIMARY KEY (`Name`),
	CONSTRAINT `fk_company_execs_CompanyCode`
	FOREIGN KEY (`CompanyCode`)
	REFERENCES `all_profiles` (`CompanyCode`)
    );



Drop table if exists aaplstockprice;
create table if not exists aaplstockprice(
    `Date` date not null,
	`High` decimal(10,6) not null,
	`Low` decimal(10,6) not null,
	`Open` decimal(10,6) not null,
	`Close` decimal(10,6) not null,
	`Volume` Varchar(45) not null,
	`Adj Close` decimal(10,6) not null,
    `Code` Varchar(45) not null,
    PRIMARY KEY (`Date`),
    CONSTRAINT `fk_aaplstockprice_Code`
	FOREIGN KEY (`Code`)
	REFERENCES `all_profiles` (`CompanyCode`)
    );



Drop table if exists amznstockprice;
create table if not exists amznstockprice(
    `Date` date not null,
	`High` decimal(10,6) not null,
	`Low` decimal(10,6) not null,
	`Open` decimal(10,6) not null,
	`Close` decimal(10,6) not null,
	`Volume` Varchar(45) not null,
	`Adj Close` decimal(10,6) not null,
    `Code` Varchar(45) not null,
    PRIMARY KEY (`Date`),
	CONSTRAINT `fk_amznstockprice_Code`
	FOREIGN KEY (`Code`)
	REFERENCES `all_profiles` (`CompanyCode`)
    );

Drop table if exists techystockprice;
create table if not exists techystockprice(
    `Date` date not null,
	`High` decimal(10,6) not null,
	`Low` decimal(10,6) not null,
	`Open` decimal(10,6) not null,
	`Close` decimal(10,6) not null,
	`Volume` Varchar(45) not null,
	`Adj Close` decimal(10,6) not null,
    `Code` Varchar(45) not null,
    PRIMARY KEY (`Date`),
	CONSTRAINT `fk_techystockprice_Code`
	FOREIGN KEY (`Code`)
	REFERENCES `all_profiles` (`CompanyCode`)
    );
    
Drop table if exists oraclestockprice;
create table if not exists oraclestockprice(
    `Date` date not null,
	`High` decimal(10,6) not null,
	`Low` decimal(10,6) not null,
	`Open` decimal(10,6) not null,
	`Close` decimal(10,6) not null,
	`Volume` Varchar(45) not null,
	`Adj Close` decimal(10,6) not null,
    `Code` Varchar(45) not null,
    PRIMARY KEY (`Date`),
	CONSTRAINT `fk_oraclestockprice_Code`
	FOREIGN KEY (`Code`)
	REFERENCES `all_profiles` (`CompanyCode`)
    );
    
Drop table if exists msftstockprice;
create table if not exists msftstockprice(
    `Date` date not null,
	`High` decimal(10,6) not null,
	`Low` decimal(10,6) not null,
	`Open` decimal(10,6) not null,
	`Close` decimal(10,6) not null,
	`Volume` Varchar(45) not null,
	`Adj Close` decimal(10,6) not null,
    `Code` Varchar(45) not null,
    PRIMARY KEY (`Date`),
	CONSTRAINT `fk_msftstockprice_Code`
	FOREIGN KEY (`Code`)
	REFERENCES `all_profiles` (`CompanyCode`)
    );

Drop table if exists intcstockprice;
create table if not exists intcstockprice(
    `Date` date not null,
	`High` decimal(10,6) not null,
	`Low` decimal(10,6) not null,
	`Open` decimal(10,6) not null,
	`Close` decimal(10,6) not null,
	`Volume` Varchar(45) not null,
	`Adj Close` decimal(10,6) not null,
    `Code` Varchar(45) not null,
    PRIMARY KEY (`Date`),
	CONSTRAINT `fk_intcstockprice_Code`
	FOREIGN KEY (`Code`)
	REFERENCES `all_profiles` (`CompanyCode`)
    );


Drop table if exists ibmstockprice;
create table if not exists ibmstockprice(
    `Date` date not null,
	`High` decimal(10,6) not null,
	`Low` decimal(10,6) not null,
	`Open` decimal(10,6) not null,
	`Close` decimal(10,6) not null,
	`Volume` Varchar(45) not null,
	`Adj Close` decimal(10,6) not null,
    `Code` Varchar(45) not null,
    PRIMARY KEY (`Date`),
	CONSTRAINT `fk_ibmstockprice_Code`
	FOREIGN KEY (`Code`)
	REFERENCES `all_profiles` (`CompanyCode`)
    );


Drop table if exists googlestockprice;
create table if not exists googlestockprice(
    `Date` date not null,
	`High` decimal(10,6) not null,
	`Low` decimal(10,6) not null,
	`Open` decimal(10,6) not null,
	`Close` decimal(10,6) not null,
	`Volume` Varchar(45) not null,
	`Adj Close` decimal(10,6) not null,
    `Code` Varchar(45) not null,
    PRIMARY KEY (`Date`),
	CONSTRAINT `fk_googlestockprice_Code`
	FOREIGN KEY (`Code`)
	REFERENCES `all_profiles` (`CompanyCode`)
    );


Drop table if exists fbstockprice;
create table if not exists fbstockprice(
    `Date` date not null,
	`High` decimal(10,6) not null,
	`Low` decimal(10,6) not null,
	`Open` decimal(10,6) not null,
	`Close` decimal(10,6) not null,
	`Volume` Varchar(45) not null,
	`Adj Close` decimal(10,6) not null,
    `Code` Varchar(45) not null,
    PRIMARY KEY (`Date`),
	CONSTRAINT `fk_fbstockprice_Code`
	FOREIGN KEY (`Code`)
	REFERENCES `all_profiles` (`CompanyCode`)
    );
