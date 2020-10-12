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
        a = self.database.find('dhruvzi', f'email = \'{self.email}\'')
        row = a[0]

        id = row['ID']
        b = self.database.find('userdata', f'user_ID = {id}')

        b = [
            {id: ..., username: ..., website: ...},
            {id: ..., username: ..., website: ...}
        ]

        return_arr = []

        for i in range(len(b)):
            current_entry = b[i]

            return_arr.append(
                {username: current_entry['username'], website: current_entry['website'], password: current_entry['password']})

        # res = map(lambda row: return {username: row['username'], website: row['website'], password: row['password']}, b)

        return return_arr  # list(res)
