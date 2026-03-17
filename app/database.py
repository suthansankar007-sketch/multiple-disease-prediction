import sqlite3

# Create DB connection
def create_connection():
    conn = sqlite3.connect("data.db")
    return conn

# Create tables
def create_tables():
    conn = create_connection()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users(
        username TEXT,
        password TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS predictions(
        username TEXT,
        disease TEXT,
        result TEXT,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()

# Add user
def add_user(username, password):
    conn = create_connection()
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?,?)", (username, password))
    conn.commit()
    conn.close()

# Login check
def login_user(username, password):
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    data = c.fetchall()
    conn.close()
    return data

# Save prediction
def save_prediction(username, disease, result, date):
    conn = create_connection()
    c = conn.cursor()
    c.execute("INSERT INTO predictions VALUES (?,?,?,?)",
              (username, disease, result, date))
    conn.commit()
    conn.close()

# Get user history
def get_predictions(username):
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM predictions WHERE username=?", (username,))
    data = c.fetchall()
    conn.close()
    return data
