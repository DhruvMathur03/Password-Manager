import sqlite3 as sql
import sys


class DB:
    con = None
    cur = None

    def __init__(self, db_name):  # constructor
        try:
            self.con = sql.connect(db_name)
            self.cur = self.con.cursor()
        except sql.Error:
            print("Error")
            sys.exit(1)

    def __del__(self):
        if self.con:
            print("Closing connection to the db")
            self.con.close()

    def select_all(self):
        all_rows = self.cur.execute("SELECT * FROM dhruvzi")

        return all_rows.fetchall()

    def fetch_column(self, table, col_name):
        all_rows = self.cur.execute(f'SELECT {col_name} FROM {table}')

        return all_rows.fetchall()

    def insert(self, table, column_values):
        s = ","
        col_names_string = s.join(column_values.keys())
        wrapped_values = map(lambda v: f'"{v}"', column_values.values())
        values = s.join(list(wrapped_values))
        sql_statement = f'INSERT INTO {table}({col_names_string}) VALUES({values})'
        print(sql_statement)
        self.cur.execute(sql_statement)
        self.con.commit()

    def find(self, table, conditions):
        # conditions: where clause condition

        sql_statement = f'SELECT * FROM {table} WHERE {conditions}'
        a = self.cur.execute(sql_statement)
        return a.fetchall()
