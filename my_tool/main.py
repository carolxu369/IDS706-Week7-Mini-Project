import sqlite3
import sys

DATABASE = "data.db"

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, content TEXT)''')

def add_data(data):
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute("INSERT INTO data (content) VALUES (?)", (data,))

def view_data():
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        for row in c.execute("SELECT * FROM data"):
            print(row)

def main():
    if len(sys.argv) < 2:
        print("Usage: my_tool <init|add|view> [data]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "init":
        init_db()
    elif command == "add":
        if len(sys.argv) < 3:
            print("Please provide data to add.")
            sys.exit(1)
        add_data(sys.argv[2])
    elif command == "view":
        view_data()
    else:
        print("Unknown command.")
        sys.exit(1)

if __name__ == "__main__":
    main()
