import sqlite3

# Skapa anslutning till databasen
conn = sqlite3.connect('todo.db')
cursor = conn.cursor()

# Skapa tabell för att lagra användarinformation
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )''')

# Skapa tabell för att lagra uppgifter i To-Do-listan
cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    task TEXT NOT NULL,
                    completed BOOLEAN NOT NULL DEFAULT False,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )''')

# Spara ändringar och stäng anslutningen
conn.commit()
conn.close()
