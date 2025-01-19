import mysql.connector
from datetime import datetime

def select_users_by_dob(dob):
    conn = mysql.connector.connect(
        host="localhost",
        user="user",
        password="password",
        database="testdb"
    )
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE dob = %s"
    start_time = datetime.now()

    cursor.execute(query, (dob,))
    users = cursor.fetchall()
    
    end_time = datetime.now()
    print(f"Time taken: {end_time - start_time}")
    print(f"Users found: {len(users)}")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    dob_to_search = "1950-01-01"
    select_users_by_dob(dob_to_search)
