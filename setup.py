cursor.execute("CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
cursor.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER, cost REAL, status TEXT, date TEXT)")