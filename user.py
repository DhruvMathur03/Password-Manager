import cli_ui
import sqlite3 as sql
import sys
import db
from prettytable import PrettyTable
from datetime import date
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from hashlib import sha256
import base64

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
        table = PrettyTable(["Website", "Username", "Password", "Date Created", "Date Modified"])

        for i in range(len(b)):
            encrypted_password = base64.b64decode(b[i][3])
            cipher = AES.new(self.email.encode()[:16], AES.MODE_CBC, iv=encrypted_password[:16])
            decrypted_password = unpad(cipher.decrypt(encrypted_password[16:]), AES.block_size).decode()
            table.add_row([b[i][1], b[i][2], decrypted_password, b[i][5], b[i][6]])
        return table

    def add_password(self, website, username, password):
        today = date.today()
        hashed_password = sha256(password.encode()).hexdigest()
        cipher = AES.new(self.email.encode()[:16], AES.MODE_CBC)
        encrypted_password = base64.b64encode(cipher.iv + cipher.encrypt(pad(hashed_password.encode(), AES.block_size)))
        self.database.insert('user_data', {
            'website': website, 'username': username, 'password': encrypted_password, 'user_ID': self.user_id, 'Date_Created': today})

    def filter_website(self, website):
        account_details = self.database.find(
            'user_data', f'website = "{website}" AND user_ID = {self.user_id}')
        table = PrettyTable(["Username", "Password", "Date Created", "Date Modified"])
        
        for i in range(len(account_details)):
            table.add_row([account_details[i][2], account_details[i][3], account_details[i][5], account_details[i][6]])
        return table

    def filter_username(self, username):
        account_details = self.database.find(
            'user_data', f'username = "{username}" AND user_ID = {self.user_id}')
        table = PrettyTable(["Website", "Password", "Date Created", "Date Modified"])

        for i in range(len(account_details)):
            table.add_row([account_details[i][1], account_details[i][3], account_details[i][5], account_details[i][6]])
        return table

    def edit_account_choice(self):
        account = self.database.find('user_data', f'user_ID = {self.user_id}')
        account_choices = []

        for i in range(len(account)):
            account_choices.append(account[i][1:3])

        choices = account_choices
        account_to_be_edited = cli_ui.ask_choice(
            "Which account would you like to edit", choices=choices)
        return account_to_be_edited    
        
    def edit(self, changes, website, username):
        new_password = changes['password']
        hashed_password = sha256(new_password.encode()).hexdigest()
        cipher = AES.new(self.email.encode()[:16], AES.MODE_CBC)
        encrypted_password = base64.b64encode(cipher.iv + cipher.encrypt(pad(hashed_password.encode(), AES.block_size)))
        changes['password'] = encrypted_password
        self.database.modify('user_data', changes,
            f'website = "{website}" AND username = "{username}"')

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
