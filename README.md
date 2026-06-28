# Password Manager
### Video Link:-  
#### Password Manager is a command-line based application written in Python that stores and manages logins/credentials. It stores credentials in JSON files locally. It allows user to create a master password to access there password and maintain security. It uses haslibs's SHA-256 hashing to secure the master password by hashing.
## Features
- Master Password authentiation
- Validates Password strength
- Add's new login
- view existing login
- delete any login
- Stored in JSON
- Validating every Input

## Project Files
### Project.py
This file contains the main login of the application. It also uses ascii art for user experience. The art aslo makes it easy to understand.Its consists various functions for handling specific roles such as authentication, menu navigation, validation, file handling, for other features etc.

### test_project.py
This file consist various test on function level. Trying to test edge cases and other possible valid and invalid inputs. It also tests the script how edge cases are handled.


## Design
### JSON instead of CSV
JSON was used instead of CSV. This design choice was made cause CSV stores data in tabular form, making it easy for table. However, JSON stores data as an object with name field such as Website Name, Website URL, Username, and Password (used in this program). JSON integrates with dictionary easily which further allows use of keys and value for searching, modifying, viewing etc.
### Hashing
Next useful design choice i made was using <ins>**haslib**</ins> library. This helped creation of master password and encoding it to hash and saving it in JSON. Making it safe from other non-owner/unofficial user to see paritcular user's password and restricting access.
### Validation
Input Validation was also implemented. To Validate user's input and to restrict invalid input  

