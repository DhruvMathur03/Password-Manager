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
        return table 

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

    def edit(self, changes):
        account = self.database.find('user_data', f'user_ID = {self.user_id}')
        website = account[0][1]
        self.database.modify('user_data', changes,
            f'website = "{website}"')

    def edit_account_choice(self):
        account = self.database.find('user_data', f'user_ID = {self.user_id}')
        account_choices = []

        for i in range(len(account)):
            account_choices.append(account[i][1:3])

        choices = account_choices
        account_to_be_edited = cli_ui.ask_choice(
            "Which account would you like to edit", choices=choices)
        
    def delete(self):
        account = self.database.find('user_data', f'user_ID = {self.user_id}')
        account_choices = []

        for i in range(len(account)):
            account_choices.append(account[i][1:3])
            
        choices = account_choices
        account_to_be_deleted = cli_ui.ask_choice(
            "Which account would you like to delete", choices=choices)
        website = account_to_be_deleted[0]
        username = account_to_be_deleted[1]
        self.database.delete('user_data',
                             f'website = "{website}" AND username = "{username}"')
