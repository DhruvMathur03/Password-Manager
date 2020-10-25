import cli_ui
import sqlite3 as sql
import sys
import db
from prettytable import PrettyTable


class User:
    email = None
    database = None
    user_id = None

    def __init__(self, user_id, email, database):
        self.email = email
        self.database = database
        self.user_id = user_id

    def get_all_password(self):
        b = self.database.find('user_data', f'user_ID = {self.user_id}')

        table = PrettyTable(["Website", "Username", "Password"])

        for i in range(len(b)):
            table.add_row(b[i][1:4])
        # res = map(lambda row: return {username: row['username'], website: row['website'], password: row['password']}, b)

        return table  # list(res)

    def add_password(self, website, username, password):
        self.database.insert('user_data', {
            'website': website, 'username': username, 'password': password, 'user_ID': self.user_id})

    def filter_website(self, website):
        account_details = self.database.find(
            'user_data', f'website = "{website}" AND user_ID = {self.user_id}')

        table = PrettyTable(["Username", "Password"])

        for i in range(len(account_details)):
            table.add_row(account_details[i][2:4])

        return table

    def filter_username(self, username):
        account_details = self.database.find(
            'user_data', f'username = "{username}" AND user_ID = {self.user_id}')
        table = PrettyTable(["Website", "Password"])

        for i in range(len(account_details)):
            table.add_row([account_details[i][1], account_details[i][3]])

        return table
