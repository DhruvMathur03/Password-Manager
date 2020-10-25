import cli_ui
import sqlite3 as sql
import sys
import db


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

        return_arr = []

        for i in range(len(b)):
            current_entry = b[i]

            return_arr.append(
                {'website': current_entry[1], 'username': current_entry[2], 'password': current_entry[3]})

        # res = map(lambda row: return {username: row['username'], website: row['website'], password: row['password']}, b)

        return return_arr  # list(res)

    def add_password(self, website, username, password):
        self.database.insert('user_data', {
            'website': website, 'username': username, 'password': password, 'user_ID': self.user_id})

    def filter_website(self, website):
        account_details = self.database.find(
            'user_data', f'website = "{website}" AND user_ID = {self.user_id}')

        final_list = []

        for i in range(len(account_details)):
            current_list = account_details[i]

            final_list.append(
                {'username': current_list[2], 'password': current_list[3]})

        return final_list

    def filter_username(self, username):
        account_details = self.database.find(
            'user_data', f'username = "{username}" AND user_ID = {self.user_id}')

        final_list = []

        for i in range(len(account_details)):
            current_list = account_details[i]

            final_list.append(
                {'website': current_list[1], 'password': current_list[3]})

        return final_list
