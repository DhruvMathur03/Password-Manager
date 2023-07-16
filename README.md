# Password-Manager

Password Manager is a secure and user-friendly application designed to store and manage your passwords. This project is built in Python and uses SQLite for database management.

## Features

### Secure Password Storage
The Password Manager securely stores all your passwords. It uses advanced encryption algorithms to ensure that your passwords are safe and cannot be accessed without proper authentication.

### Easy Retrieval of Passwords
With the Password Manager, you no longer need to remember all your passwords. The application provides a simple and efficient way to retrieve your passwords whenever you need them. Just search for the account or application name, and your password will be displayed.

### User-Friendly Interface
The Password Manager has a simple and intuitive user interface. It's designed to be easy to use, even for people who aren't tech-savvy. The commands and prompts are clear and straightforward, making password management a breeze.

### SQLite Database for Efficient Management
The application uses SQLite for database management. This allows for efficient storage, retrieval, and management of password data. SQLite databases are stored in a single file, making it easy to manage and backup your data.

### Password Generator
The Password Manager includes a built-in password generator. This feature allows you to create strong, secure passwords that are hard to crack. You can customize the length and complexity of the generated passwords to meet your needs.

### Advanced Encryption with AES and SHA-256
Password Manager employs advanced encryption techniques to ensure the security of your data. It uses the AES (Advanced Encryption Standard) and SHA-256 (Secure Hash Algorithm 256-bit) for encryption and hashing respectively. These are implemented through the use of the 'Pycryptodome' and 'hashlib' libraries.
\\
Passwords are not stored in plain text, but are encrypted using AES before being stored in the database. Additionally, SHA-256 is used for hashing critical data to ensure integrity and security. This means that even if someone were to gain access to the database file, they would not be able to read your passwords without the encryption key. This adds an additional layer of security, protecting your data even in the event of a breach.

### Multi-User Support
The Password Manager supports multiple users. Each user has their own separate and secure space for password storage. This makes it ideal for shared devices or for people who want to keep their work and personal passwords separate.
