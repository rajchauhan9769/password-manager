import time, json
import hashlib
def main():
    try:
        print("Please add password to keep you Logins safe")
        with open("master.json","r") as file:
            pre_data = json.load(file)
    except(json.JSONDecodeError, FileNotFoundError):
        with open("master.json","w") as file:
            print("You don't have existing password.")
            add_password = input("Please add password: ")
            hash_password = {"master_hash":hashlib.sha256(add_password.encode()).hexdigest()}
            json.dump(hash_password,file)
            print("Password saved successfully.")
    else:     
        master_password()
def master_password():
    attempt = 0
    while attempt < 3:
        login_password = input("Enter Master Password: ")
        hash_login = hashlib.sha256(login_password.encode()).hexdigest()
        with open("master.json","r") as file:
            data = json.load(file)

        if hash_login == data["master_hash"]:
            main_menu()
            break
        print("Incorrect Password. Try Again.")
        attempt += 1
    else:
        print("Too many attempts.")
def main_menu():
    print("Welcome to Password Manager")
    print("Loading...")
    time.sleep(0.5)
    #===========
    # Menu Bar 
    #===========
    print("1. Add Login")
    print("2. View Logins")
    print("3. Search Login")
    print("4. Delete Login")
    print("""
======================
      Main Menu
======================
----------------------
    1. Add Login
----------------------
    2. View Logins
----------------------
    3. Search Login
----------------------
    4. Delete Login
----------------------
""")
    #===================
    # Select Operations
    #===================
    initial_input = input("""
======================
 Type 1, 2, 3 or 4: 
======================
""")
    #===========================
    #Option Selection Condition
    #===========================
    if initial_input == "1":
        #Website Name
        webname = input("Enter Website's Name: ")
        website_namehandling(webname)
        #Website Url
        weburl = input("Enter Wesites Url: ")
        website_urlhandling(weburl)
        #Calling "username" Function 
        user_name = input("Enter Username: ")
        print(username_handling(user_name))
        
        time.sleep(0.5)
        # Requirements
        print("Password should contain atleast [1 - capital character] [1 - small character] [1 - special character] and more than [8 - characters ]")
        #========================================
        # Calling "password_handling" Function
        #=======================================
    
        password_handling(user_name, webname, weburl)
    elif initial_input == "2":
        view()
    
    elif initial_input == "3":
        #========================================
        # Calling "Searching" Function
        #=======================================
        account_name =  input("Enter Website name: ")
        data = searching(account_name)
        # =======================
        # Modifying print for UX 
        # =======================
        if data == "Credential does not exist.":
            print("Wrong input")
        else:
            print(f"""
============================
        Search Results
============================
----------------------------                         
Website Name : {data["Website Name"]}
----------------------------
Website Url  : {data["Website Url"]}
----------------------------
Username     : {data["Username"]}
----------------------------
Password     : {data["Password"]}
----------------------------
        """)
    elif initial_input == "4":
        #========================================================================================
        #Calling "Searching" Function again to delete the data by reusing the searching function
        #========================================================================================
        account_delete = input("Name the Login you want to delete: ")
        result = searching(account_delete)
        if result == "Credential does not exist.":
            print(result)
        else:
            delete(result)

#======================
# Website Name Feature
#======================
def website_namehandling(webname):
    print(webname.capitalize())

#============================
# Website Url Handling Feature
#============================
def website_urlhandling(weburl):       #**** Website Url Validation upcoming ****
    print(weburl)

#======================
# Username 
#======================
def username_handling(user_name):               #****Username Validation upcoming.****
    return "Username Added Successfully"


#============================================
# Password Confirming and intiating for json
#============================================
def password_handling(user_name, webname, weburl):    
    # Confirming Password.
    # Loop for mismatched password until it matches.
    attempt_password = 0
    while attempt_password < 3:
        print("Attempt No:",attempt_password)
        password = input("Enter Password: ")
        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False
        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
            elif not char.isalnum():
                has_special = True
        if len(password)>= 8 and has_upper and has_lower and has_special and has_digit == True:
            print("Your password is Valid.")
            attempt = 0
            while attempt < 3:
                re_enter = input("Re-enter Password: ")   
                if password == re_enter:
                    print("Password Added Successfully.")
                    time.sleep(0.5)
                    #Save Password
                    print("Do you want to save your password.")
                    # Creating "save" Function and confirming to save or not.
                    response = input("Enter [Y] - Yes or [N] - No: ")
                    save_permanent(response,password, user_name, webname, weburl)
                    break
                print("Password mismatched please re-enter.")
                attempt += 1
            else:
                print("Password Confirmation failed")
            break
        else:
            print(
"""
==============================
==============================
Following things are missing:
==============================
==============================
""")
            if not len(password) >= 8:
                print("""
++++++++++++++++++++++
Password is too small.
++++++++++++++++++++++                      
                      """)
            if not has_upper :
                print("""
+++++++++++++++++++++++++++
Uppercase letter is missing
+++++++++++++++++++++++++++                      
""") 
            if not has_lower :
                print("""
+++++++++++++++++
Lower is missing.
+++++++++++++++++""")
            if not has_digit :
                print("""
+++++++++++++++++++++++++++
Digits are missing.
+++++++++++++++++++++++++++""")
            if not has_special:
                print("""
+++++++++++++++++++++++++++++
Special Character is missing.
+++++++++++++++++++++++++++++
                      """)
        attempt_password += 1
    else:
        print("Number of attempts Exceeded")
        
#===========================================
#Json File Handling 
#Permanent saving of Logins in Json.
#===========================================
def save_permanent(response, password, user_name, webname, weburl):
    if response == "Y":
        try:
            with open("save.json","r") as file:
                existing_data = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
                with open("save.json","a") as file:
                    existing_data = []
        existing_data.append({
        "Website Name": webname,
        "Website Url": weburl,
        "Username": user_name,
        "Password": password,
            })
        with open("save.json","w") as file:
            json.dump(existing_data,file,indent="\t")
        print("Password Saved Successfully!!")
    else:
        print("Your Password is Terminated")


#===========================================
#Viewing Saved Password
#===========================================
def view():
    with open("save.json","r") as file:
        datas = json.load(file)
    for data in datas:
        print(
f"""
{data["Website Name"]} :-
================================
Website  : {data["Website Name"]}
URL     : {data["Website Url"]}
Username : {data["Username"]}
Password : {data["Password"]}
================================""")
        

#=====================================
#Block used for searching the account
#=====================================
def searching(account_name):
    with open("save.json","r") as file :
        datas = json.load(file)
    for data in datas:
        if data["Website Name"].lower() == account_name.lower():
            return(data)
    else:
        return("Credential does not exist.")
#===========================================
#Block used for deleting a particular Login 
#===========================================
def delete(account_delete):
    with open("save.json","r") as file :
        datas = json.load(file)
    print(f"Are you sure you want to delete: {account_delete}")
    delete_input = input("Enter [Y] - Yes or [N] - No: ") 
    for data in datas:
        if not delete_input == "Y" or "N":
            print("Wrong input")
            break
        if delete_input == "N":
            print("Delete process was Terminated.")
            break
        if delete_input == "Y":
            if data == account_delete:
                datas.remove(account_delete)
                with open("save.json","w") as file:
                    json.dump(datas,file,indent="\t")
                print("Data was deleted successfully.")
       
    
if __name__ == "__main__":
    main()