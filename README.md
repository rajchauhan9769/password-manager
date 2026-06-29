# Password Manager

### Video Link:

## Description

#### Password Manager is a command-line application written in Python that allows users to securely store and manage login credentials. The application stores credentials in JSON files locally. It allows users to create a master password to access their passwords and maintain security. The application uses Python's **hashlib** library's SHA-256 hashing algorithm to secure and protect the master password by hashing.

#### It is my first ever coding project, developed as my final project for CS50P. While building this project, I combined multiple Python concepts into one practical application which I learned throughout my CS50P journey. This project gave me hands-on experience with functions, loops, conditionals, file handling, exception handling, dictionaries, JSON, hashing, etc.

## Program Workflow

When the application is executed for the first time, it checks whether the user is an existing user or a new user by checking whether any `master.json` (master password) file already exists or not.

If not, it asks the user to create a master password. The master password should satisfy its strength requirements, making the user create a strong password. Once a strong password is created, it hashes the password and saves it to the `master.json` file, making it secure for the user.

Once this authentication process is done, the user is introduced to a menu where different tasks such as adding credentials, viewing saved credentials, searching for specific credentials from the saved ones, deleting any saved credentials, etc. can be performed.

## Features

- Master Password authentication
- Validates Password strength
- Add new logins
- View existing logins
- Delete saved logins
- Store credentials in JSON
- Input Validation

## Project Files

### <ins>Project.py</ins>

This file contains the main logic of the application. It also displays ASCII art to improve the user experience. The art also makes it easy to understand. It consists of various functions for handling specific roles such as authentication, menu navigation, validation, file handling, and other features.

### <ins>test_project.py</ins>

This file contains pytest test cases for the validation functions. The tests cover valid inputs, invalid inputs, and several edge cases to ensure the application behaves correctly.

## Design

### <ins>JSON instead of CSV</ins>

JSON was used instead of CSV. This design choice was made because CSV stores data in tabular form, making it suitable for tables. However, JSON stores data as objects with named fields such as Website Name, Website URL, Username, and Password (used in this program). JSON integrates with dictionaries easily, which further allows the use of keys and values for searching, modifying, viewing, etc.

### <ins>Hashing</ins>

The next useful design choice I made was using Python's **hashlib** library.

Initially, I considered hashing every password and credential of a website. But after researching hashing, I learned that hashing is a one-way process, and unlike encryption-decryption, it cannot be recovered once hashed. It can only be matched with the hash of the same password.

This helped in the creation of the master password and hashing it before saving it in JSON, making it safe from non-owners or unauthorized users from seeing a particular user's password and restricting access.

### <ins>Validation</ins>

Input validation was also implemented to validate user input and restrict invalid input. It also helps prevent unusual crashes. It also provides responses to every valid and invalid user input, which further improves the user experience.

I used validation such as website names and usernames cannot be empty; they should contain at least one alphabetic letter. Passwords must satisfy their validation requirements to create a strong password. URLs must satisfy their own validation rules by having a proper URL.

## Challenges

During this project, I encountered different challenges, such as not knowing much about JSON files, so I needed to understand them and go through the documentation. Another challenge was that I didn't know how to structure the code, so instead of creating one large block, I used different functions, each having a specific task. Using different functions improved readability and caused less confusion during coding.

## Library Used

### <ins>json</ins>

Used to store and retrieve credentials from local JSON files. Also used for the master password.

### <ins>hashlib</ins>

Used to hash the master password using the SHA-256 hashing algorithm, making the master password more secure.

### <ins>time</ins>

Used to create small delays that improve the user experience during program execution.

## Future Version

If I continue developing this project, I would add several new features, including:

- Password encryption for stored credentials.
- Password generator.
- Edit or update existing credentials.
- Stronger URL validation.
- Graphical user interface.
- A web version of the application using the MERN stack.
