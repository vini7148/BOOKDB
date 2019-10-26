# BOOKDB

This repository contains the front end using python for managing books using the SQL server

## Getting started

clone this repository using
```
git clone https://github.com/vini7148/BOOKDB.git
cd BOOKDB
```

### Prerequisites

The following tools along with basic knowledge of python and SQL is required to execute this front end
```
python==3.7.3
pypyodbc==1.3.5
Microsoft sql server 2017
```

You can download these needed file using the links below

* [python==3.7.3](https://www.python.org/ftp/python/3.8.0/python-3.8.0.exe)
* [pypyodbc==1.3.5](https://pypi.org/project/pypyodbc/)
* [Microsoft sql server 2017](https://go.microsoft.com/fwlink/?linkid=853017)

### Installing

First you need to activate the python virtual environment (venv)
```
python -m venv 'name of the env' (already present in this repository)
```
To activate this env
* On windows (using git bash)
```
source 'name of the env'/Scripts/activate 
```
* On Unix/Linux
```
source 'name of the env'/Scripts/activate 
```
* On mac
```
source bin/activate
```


### Running

Now you can execute the front end application by
```
mybooks.py
```

**NOTE**: *Before running the application please complete the empty fields in the sqlserver_config.py file, all fields are necessary and should be properly filed before executing the mybooks.py application*

## ScreenShot

![MYBOOKS](https://github.com/vini7148/BOOKDB/blob/master/screenshots/ss1.png)

## Deployment

This application or the front end can be used to store the details of different books and a few alterations to the code can make this application to be used for any form of datastorage where the user can insert, modify and delete records in SQL databases with the click of a few onscreen buttons instead of the long SQL queries

## Built with

* [PYTHON](https://www.python.org/)
* [PYPYODBC](https://pypi.org/project/pypyodbc/)
* [MICOSOFT SQL SERVER 2017](https://www.microsoft.com/en-us/sql-server/sql-server-2017)

## Authors

* **Vinayak Goswami** - *Initial work* - [vini7148](https://github.com/vini7148)