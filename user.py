import cli_ui
import sqlite3 as sql
import sys
import db


class User:
    email = None
    database = None

    def __init__(self, email, database):
        self.email = email
        self.database = database

    def get_all_password(self):

        a = self.database.find('Users', f'email = \'{self.email}\'')
        row = a[0]

        id = row[0]
        b = self.database.find('user_data', f'user_ID = {id}')

        return_arr = []

        for i in range(len(b)):
            current_entry = b[i]

            return_arr.append(
                {'website': current_entry[1], 'username': current_entry[2], 'password': current_entry[3]})

            # res = map(lambda row: return {username: row['username'], website: row['website'], password: row['password']}, b)

            return return_arr  # list(res)
