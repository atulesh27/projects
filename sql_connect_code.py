import mysql.connector

# Decorator function for database connection
def db_connection(func):
    def wrapper(*args, **kwargs):
        try:
            # Establish a database connection
            db = mysql.connector.connect(
                host='DESKTOP-56RSNME',
                database='orm_database',
                user='root',
                password='Saurabh@027'
            )

            # Create a cursor to execute SQL queries
            cursor = db.cursor()

            # Call the wrapped function with the cursor and any additional arguments
            result = func(cursor, *args, **kwargs)

            # Commit the changes to the database
            db.commit()

            # Close the cursor and database connection
            cursor.close()
            db.close()

            return result
        except Exception as e:
            # Handle any database-related exceptions and return an empty list
            print(f"Database error: {e}")
            return []

    return wrapper

# Function to fetch data from the database
@db_connection
def fetch_data_from_db(cursor):
    try:
        # Execute an SQL query to retrieve data from the ormapp_ormmodel table
        cursor.execute("SELECT * FROM ormapp_ormmodel")

        # Fetch all the rows from the result set
        data = cursor.fetchall()

        return data
    except Exception as e:
        print(f"Query error: {e}")
        return []

if __name__ == "__main__":
    # Call the function to fetch data from the database
    fetch_data = fetch_data_from_db()

    # Iterate over the fetched data and print each row
    for row in fetch_data:
        print(row)

