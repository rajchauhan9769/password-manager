import time, json
import hashlib
print(""" 
██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝

███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗
████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
""")
time.sleep(0.3)
def main():
    try:
        with open("master.json","r") as file:
            pre_data = json.load(file)
    except(json.JSONDecodeError, FileNotFoundError):
        with open("master.json","w") as file:
            print("""
>> Status: NEW USER DETECTED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Initializing Password Manager 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
            time.sleep(0.3)
            print("""
────────────────────────────────────────

Create a Master Password to secure
your vault and continue.

────────────────────────────────────────
""")              
            print("""
────────────────────────────────────────
Password Requirements:
• 8+ characters
• Uppercase letter
• Lowercase letter
• Digit
• Special character
──────────────────────────────────────── """)
            attempt_password = 1
            while attempt_password <= 3:
                add_password = input("""
────────────────────
Please add password: 
────────────────────                            
>""")
                
                has_upper = False
                has_lower = False
                has_digit = False
                has_special = False
                for char in add_password:
                    if char.isupper():
                        has_upper = True
                    elif char.islower():
                        has_lower = True
                    elif char.isdigit():
                        has_digit = True
                    elif not char.isalnum():
                        has_special = True
                if len(add_password)>= 8 and has_upper and has_lower and has_special and has_digit:
                    print("""
════════════════════════════════════════

>> Status: PASSWORD VERIFIED 
All validation checks passed successfully.

════════════════════════════════════════""")
                    hash_password = {"master_hash":hashlib.sha256(add_password. encode()).hexdigest()}
                    json.dump(hash_password,file)
                    print("""
════════════════════════════
>> Status: PASSWORD SAVED
════════════════════════════
""")
                    main_menu()
                    return 
                else:
                    print(
"""
++++++++++++++++++++++++++++++++

       VALIDATION FAILED        

++++++++++++++++++++++++++++++++
      
Missing requirements:""",end="")
                    if not len(add_password) >= 8:
                            print("""
++++++++++++++++++++++
Password is too small.
++++++++++++++++++++++""")
                    if not has_upper :
                            print(
"""+++++++++++++++++++++++++++
Uppercase letter is missing
+++++++++++++++++++++++++++""") 
                    if not has_lower :
                            print(
"""+++++++++++++++++
Lower is missing.
+++++++++++++++++""")
                    if not has_digit :
                            print(
"""++++++++++++++++++++
Digits are missing.
++++++++++++++++++++""")
                    if not has_special:
                            print(
"""+++++++++++++++++++++++++++++
Special Character is missing.
+++++++++++++++++++++++++++++""")
                attempt_password += 1
            else:
                print(f"""
═════════════════                     
⚠ Attempt {attempt_password} of 3
═════════════════""")
                print("""
════════════════════════════════════════

>> Status: ATTEMPT LIMIT EXCEEDED

Maximum number of attempts reached.

════════════════════════════════════════""")
    else:     
        master_password()
def master_password():
    attempt = 0
    while attempt < 3:
        login_password = input("""
───────────────────────
Enter Master Password: 
───────────────────────
=>""")
        if login_password == "":
            print("""
>> Status: INPUT REQUIRED 
Master Password cannot be empty.
""")
            continue
        hash_login = hashlib.sha256(login_password.encode()).hexdigest()
        with open("master.json","r") as file:
            data = json.load(file)

        if hash_login == data["master_hash"]:
            main_menu()
            break
        print("""
>> Status: ACCESS DENIED
Incorrect Password. Try Again.
""")
        attempt += 1
    else:
        print("Too many attempts.")
def main_menu():
    print("\nLoading...")
    time.sleep(0.5)
    print(""" 
>> Status: ACCESS GRANTED 
╔═══════════════════════════════════════════════════════════╗
║   W E L C O M E   T O   P A S S W O R D   M A N A G E R   ║
╚═══════════════════════════════════════════════════════════╝
""")
    #===================
    # Select Operations
    #===================
    while True:
        initial_input = input("""
════════════════════════
      Main Menu
════════════════════════
────────────────────────
    1. Add Login
────────────────────────
    2. View Logins
────────────────────────
    3. Search Login
────────────────────────
    4. Delete Login
────────────────────────
    5. Exit
────────────────────────
      
────────────────────────
Type 1, 2, 3, 4, or 5 : 
────────────────────────
=>""")
# ===================================================================================
        #===========================
        #Option Selection Condition
        #===========================
        if initial_input == "1":
            #Website Name
            while True:
                webname = input("""
═════════════════════
Enter Website's Name: 
═════════════════════
>""")
                if website_namehandling(webname):
                    break
# ======================================================================================
              
            # ===========
            # Website Url
            # ============
            while True:
                weburl = input("""
══════════════════
Enter Wesites Url: 
══════════════════
>""")           
                if website_urlhandling(weburl): 
                    break
            

# =======================================================================================
            # ===========================
            # Calling "username" Function 
            # ===========================
            while True:
                user_name = input("""
═══════════════
Enter Username: 
═══════════════
>""")
                if username_handling(user_name):
                    break
            
            time.sleep(0.5)
# =======================================================================================
            # Requirements
            print("""
────────────────────────────────────────
Password Requirements:
• 8+ characters
• Uppercase letter
• Lowercase letter
• Digit
• Special character
────────────────────────────────────────     
""")
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
                print(data)
            elif data == "No saved credentials found.":
                print(data)
            else:
                print(f"""
════════════════════════════
        Search Results
════════════════════════════
────────────────────────────                         
Website Name : {data["Website Name"]}
────────────────────────────
Website Url  : {data["Website Url"]}
────────────────────────────
Username     : {data["Username"]}
────────────────────────────
Password     : {data["Password"]}
────────────────────────────
            """)
        elif initial_input == "4":
            #========================================================================================
            #Calling "Searching" Function again to delete the data by reusing the searching function
            #========================================================================================
            delete()
        elif initial_input == "5":
            print("""

════════════════════════════════════════

>> Status: SESSION ENDED

Thank you for using Password Manager.

════════════════════════════════════════

""")
            break
            
        else:
            print("""
++++++++++++++++++++++++++++++++++++++++

>> Status: INVALID INPUT

Please select a valid option.

++++++++++++++++++++++++++++++++++++++++
""")


#======================
# Website Name Feature
#======================
def website_namehandling(webname):
        if webname.strip() == "":
            print("Website name cannot be empty.")
            return False
        return True 

#============================
# Website Url Handling Feature
#============================
def website_urlhandling(weburl):       #**** Website Url Validation upcoming ****
        if "." not in weburl:
            print("Not a Valid url")
            return False
        return True



#======================
# Username 
#======================
def username_handling(user_name):               #****Username Validation upcoming.****
        if user_name.strip() == "":
            print("Username cannot be empty.")
            return False
        return True

#============================================
# Password Confirming and intiating for json
#============================================
def password_handling(user_name, webname, weburl):    
    # Confirming Password.
    # Loop for mismatched password until it matches.
    attempt_password = 1
    while attempt_password <= 3:
        password = input("""
────────────────────
Enter Password:
────────────────────
>""")
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
        if len(password)>= 8 and has_upper and has_lower and has_special and has_digit:
            print("""
>> Status: PASSWORD VERIFIED
All validation checks passed successfully.""")
            attempt = 0
            while attempt < 3:
                re_enter = input("""
────────────────────
Re-enter Password:
────────────────────
>""")   
                if password == re_enter:
                    print("Password Added Successfully.")
                    time.sleep(0.5)
                    #Save Password
                    
                        
                    save_permanent(password, user_name, webname, weburl)
                    break
                print("""
>> Status: PASSWORD MISMATCHED""")
                attempt += 1
            else:
                print("Password Confirmation failed")
            break
        else:
            print(f"""
═════════════════                    
⚠ Attempt {attempt_password} of 3
═════════════════""")
            print(
"""
++++++++++++++++++++++++++++++++++++++++

       VALIDATION FAILED

++++++++++++++++++++++++++++++++++++++++

Missing requirements:
""")
            if not len(password) >= 8:
                print("""
++++++++++++++++++++++
Password is too small.
++++++++++++++++++++++""")
            if not has_upper :
                print("""
+++++++++++++++++++++++++++
Uppercase letter is missing
+++++++++++++++++++++++++++""") 
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
+++++++++++++++++++++++++++++""")
        attempt_password += 1
    else:
        print("""
════════════════════════════════════════

>> Status: ATTEMPT LIMIT EXCEEDED

Maximum number of attempts reached.

════════════════════════════════════════""")
        
#===========================================
#Json File Handling 
#Permanent saving of Logins in Json.
#===========================================
def save_permanent(password, user_name, webname, weburl):
    print("Do you want to save your password.")
    # Creating "save" Function and confirming to save or not.
    while True:
        response = input("Enter [Y] - Yes or [N] - No: ").upper()
        if response in ["Y","N"]:
            break
        print("Invalid Input")
    while True:
        if response == "Y":
            try:
                with open("save.json","r") as file:
                    existing_data = json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
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
            break
        elif response == "N":
            print("Your Password is Terminated")
            break
        else:
            print("Invalid Input")


#===========================================
#Viewing Saved Password
#===========================================
def view():
    try:
        with open("save.json","r") as file:
            datas = json.load(file)
        for data in datas:
            print(
f"""
{data["Website Name"]} :-
════════════════════════════════
Website  : {data["Website Name"]}
URL     : {data["Website Url"]}
Username : {data["Username"]}
Password : {data["Password"]}
════════════════════════════════""")
    except (json.JSONDecodeError, FileNotFoundError):
        print("No saved credentials found.")
        

#=====================================
#Block used for searching the account
#=====================================
def searching(account_name):
    try:
        with open("save.json","r") as file :
            datas = json.load(file)
        for data in datas:
            if data["Website Name"].lower() == account_name.lower():
                return(data)
        else:
            return("Credential does not exist.")
    except(json.JSONDecodeError, FileNotFoundError):
        return "No saved credentials found."
#===========================================
#Block used for deleting a particular Login 
#===========================================
def delete():
        account_delete = input("Name the Login you want to delete: ")
        result = searching(account_delete)
        if result == """
⚠ Credential does not exist.""":
            print(result)       
        else:
                try:
                    with open("save.json","r") as file :
                        datas = json.load(file)
                    print("""
            ────────────────────────────────────────
                      DELETE CONFIRMATION
            ────────────────────────────────────────
            """)
                    print(f"""Selected Account:- 
{result["Website Name"]} :-
════════════════════════════════
Website  : {result["Website Name"]}
URL     : {result["Website Url"]}
Username : {result["Username"]}
Password : {result["Password"]}
════════════════════════════════""")
                    
                    while True:
                            delete_input = input("Enter [Y] - Yes or [N] - No: ") 
                            if delete_input not in  ["Y" , "N"]:
                                    print("Wrong input")
                            elif delete_input == "N":
                                print("Delete process was Terminated.")
                                break
                            else:
                                if delete_input == "Y":
                                    for data in datas:
                                        if data == result:
                                            datas.remove(result)
                                            with open("save.json","w") as file:
                                                json.dump(datas,file,indent="\t")
                                            print("Data was deleted successfully.")
                                break
                            
                except(json.JSONDecodeError, FileNotFoundError):
                    print("No saved credentials found.")
                
if __name__ == "__main__":
    main()