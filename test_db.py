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

    def insert(self, table, column_values):
        # column_values = {'useranem': 'dhruv', 'password': 'yash', 'email': 'sadbhjasbdj@njfsd.com'}
        # columns_name = column_values.keys()
        # c1, c2, c3
        # v1, v2, v3

        # {'c1': v1, }.
        # column_names = ['username', 'password', 'email'] => "username, password, email"
        # values = "dhruv, yash, sdjhfbdsjhfbdsjh@ngsjdk.com"
        s = ","
        col_names_string = s.join(column_values.keys())
        values = s.join(column_values.values())
        sql_statement = f'INSERT INTO {table}({col_names_string}) VALUES({values})'
        print(sql_statement)
        self.cur.execute(sql_statement)
        self.con.commit()


db = DB("pugsey.db")

db.insert('dhruvzi', {'id': '10', 'pugs': '99'})
a = db.select_all()

print(a)
#con = None
# try:
#    con = sql.connect('pugsey.db')
#    cur = con.cursor()
#    cur.execute('CREATE TABLE dhruvzi(id INT, pugs INT)')
# except sql.Error:
#    print("Error")
#    sys.exit(1)
# finally:
# if con:
#    con.close()
