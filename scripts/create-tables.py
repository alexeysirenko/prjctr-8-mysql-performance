import mysql.connector

def create_table():
    conn = mysql.connector.connect(
        host="localhost",
        user="user",
        password="password",
        database="testdb"
    )
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            dob DATE NOT NULL
        );
    """)
    print("Table 'users' created.")
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_table()
