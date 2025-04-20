import pyodbc

def connect_to_azure():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=your_server.database.windows.net;'
        'DATABASE=your_db;'
        'UID=your_user;'
        'PWD=your_password'
    )

def insert_expense(data):
    conn = connect_to_azure()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO expenses (amount, category, date) VALUES (?, ?, ?)",
        data['amount'], data['category'], data['date']
    )
    conn.commit()
    conn.close()