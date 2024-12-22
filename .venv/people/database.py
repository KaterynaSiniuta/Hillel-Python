import sqlite3
from person import Person
from datetime import datetime

class Database:
    def __init__(self, db_name="people.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS people (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT,
                middle_name TEXT,
                birth_date TEXT,
                death_date TEXT,
                gender TEXT
            )
        """)
        self.conn.commit()

    def add_person(self, person):
        self.cursor.execute("""
            INSERT INTO people (first_name, last_name, middle_name, birth_date, death_date, gender)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (person.first_name, person.last_name, person.middle_name,
              person.birth_date.strftime("%Y-%m-%d") if person.birth_date else None,
              person.death_date.strftime("%Y-%m-%d") if person.death_date else None,
              person.gender))
        self.conn.commit()

    def search_people(self, query):
        self.cursor.execute("""
            SELECT first_name, last_name, middle_name, birth_date, death_date, gender
            FROM people
            WHERE first_name LIKE ? 
            OR last_name LIKE ? 
            OR middle_name LIKE ?
        """, (query + '%', query + '%', query + '%'))
        rows = self.cursor.fetchall()
        return [Person(*row) for row in rows]

    def load_all(self):
        self.cursor.execute("SELECT first_name, last_name, middle_name, birth_date, death_date, gender FROM people")
        rows = self.cursor.fetchall()
        return [Person(*row) for row in rows]

    def close(self):
        self.conn.close()

