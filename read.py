import sqlite3

def get_questions(category):
    # Connect to the database
    conn = sqlite3.connect('database.sql.db')
    c = conn.cursor()

    # Retrieve questions for the specified category
    c.execute(f"SELECT * FROM {category}")
    questions = c.fetchall()

    # Close the connection
    conn.close()

    return questions