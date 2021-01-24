# Overview

This is a basic program to manage customers and orders utilizing an SQLite database in Python.

My goal in the development of this software was to learn the basic commands of the SQLite module, including how to:
* CREATE tables within a database
* SELECT, INSERT, UPDATE, and DELETE of data from within a table
* querey data using WHERE and ORDER BY
* aggregate numerical data using SUM

The program is designed with the intention to store, and allow for the retrieval of, a customer's **ID**, **name** and **email**, along with orders containing an **order ID**, **customer ID**, **cost**, **status**, and **date** of entry.

For a walkthrough of the code and a demonstration of the software, click on the hyperlink below:

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

* Customer Table 
    * id INTEGER PRIMARY KEY
    * name TEXT
    * email TEXT
* Order Table
    * id INTEGER PRIMARY KEY
    * customer_id INTEGER
    * cost REAL
    * status TEXT
    * date

# Development Environment

* Visual Studio Code
* Python 3.8.5
* sqlite3

# Useful Websites

* [SQLite Python3 API Documentation](https://docs.python.org/3/library/sqlite3.html)
* [Additional SQLite Command Help : TutorialsPoint](https://www.tutorialspoint.com/sqlite/sqlite_python.htm)

# Future Work

* adding the ability to view all active customer orders by use of INNER JOIN to view data from two tables within a single database
* adding both a customer and order submenu to increase ease of use and organization