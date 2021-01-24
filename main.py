import sqlite3

def display_customer_submenu():
    print("""
    1. Add new customer
    2. Display all customers
    3. Update customer information
    4. Display customer orders
    5. Delete a customer
    6. RETURN TO MAIN MENU
    """)

def display_orders_submenu():
    print("""
    1. Add new order
    2. View all orders
    3. View orders recently shipped
    4. Update order status
    5. Display invoice
    6. RETURN TO MAIN MENU
    """)

# Display table of commands
def display_table():
    #print("""
    #1. Customer menu
    #2. Order menu
    #""")
    
    print("""
    ORDERS
    1. Add new order.
    2. View all orders.
    3. View orders recently shipped.

    CUSTOMERS
    4. Add new customer.
    5. Display all customers.
    6. Update customer information.
    7. Delete a customer.

    OPTIONS
    8. Display invoice.
    9. Quit.
    """)


def add_order():
    customer_id = input("Customer ID: ")
    cost = input("Cost: ")
    status = input("Status: ")
    date = input("Date: ")
    values = (customer_id, cost, status, date)
    cursor.execute("INSERT INTO orders (customer_id, cost, status, date) VALUES (?,?,?,?)", values)
    connection.commit()


def display_orders():
    cursor.execute("SELECT * FROM orders")
    print("{:<5} {:<5} {:<10} {:<10} {:<10}".format("ID", "CID", "Cost", "Status", "Date"))
    for order in cursor.fetchall():
        print("{:<5} {:<5} {:<10} {:<10} {:<10}".format(order[0], order[1], order[2], order[3], order[4]))


def display_recent_orders():
    cursor.execute("SELECT * FROM orders WHERE status LIKE '%Shipped%' ORDER BY date(date) DESC Limit 14")
    for order in cursor.fetchall():
        print("{:<5} {:<5} {:<10} {:<10} {:<10}".format(order[0], order[1], order[2], order[3], order[4]))


def add_customer():
    name = input("Name: ")
    email = input("Email: ")
    values = (name, email)
    cursor.execute("INSERT INTO customers (name, email) VALUES (?,?)", values)
    connection.commit()


def display_customers():
    cursor.execute("SELECT * FROM customers")
    print("{:<5} {:<20} {:<20}".format("ID", "Name", "Email"))
    for customer in cursor.fetchall():
        print("{:<5} {:<20} {:<20}".format(customer[0], customer[1], customer[2]))


def update_customer():
    name = input("Name: ")
    email = input("Email: ")
    values = (email, name)
    cursor.execute("UPDATE customers SET email = ? WHERE name = ?", values)
    connection.commit()


def delete_customer():
    name = input("Name: ")
    values = (name, )
    cursor.execute("DELETE FROM customers WHERE name = ?", values)
    connection.commit()


def display_invoice():
    cursor.execute("SELECT SUM(cost) FROM orders")
    for sum in cursor.fetchall():
        for value in sum:
            print("Total: $" + str("{:.2f}".format(value)))

# Open connection to database
connection = sqlite3.connect('store.db')
cursor = connection.cursor()

while True:

    display_table()
    choice = input("Please input a number: ")

    if choice == "1":
        add_order()
    elif choice == "2":
        display_orders()
    elif choice == "3":
        display_recent_orders()
    elif choice == "4":
        add_customer()
    elif choice == "5":
        display_customers()
    elif choice == "6":
        update_customer()
    elif choice == "7":
        delete_customer()
    elif choice == "8":
        display_invoice()
    elif choice == "9":
        break
    else:
        print("Please input a valid number.\n")
        continue
    
# Close connection to database
connection.close()

print("Connection closed.\n")