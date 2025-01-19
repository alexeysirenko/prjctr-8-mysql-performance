import mysql.connector
from datetime import date, datetime, timedelta
import random

def add_users():
    conn = mysql.connector.connect(
        host="localhost",
        user="user",
        password="password",
        database="testdb"
    )
    cursor = conn.cursor()

    query = "INSERT INTO users (name, dob) VALUES (%s, %s)"
    batch_size = 1
    total_users = 50
    start_date = date(1950, 1, 1)
    end_date = date(2000, 1, 1)
    delta = end_date - start_date
    start_time = datetime.now()

    for i in range(0, total_users, batch_size):
        batch = [
            (
                f"User_{j}",
                start_date + timedelta(days=random.randint(0, delta.days))
            )
            for j in range(i, i + batch_size)
        ]
        cursor.executemany(query, batch)
        conn.commit()
        print(f"{i + len(batch)} users added.")
    
    end_time = datetime.now()
    print(f"Time taken: {end_time - start_time}")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    add_users()
