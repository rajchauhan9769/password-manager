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
    # Menu Bar 
    print("1. Add Login")
    print("2. View Logins")
    print("3. Search Login")
    print("4. Delete Login")
    # Select Operations
    initial_input = input("Type 1, 2, 3 or 4: ")
    #Option Selection Condition
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
        password = input("Enter Password: ")
        password_handling(password, user_name, webname, weburl)
    elif initial_input == "2":
        view()
    
    elif initial_input == "3":
        account_name =  input("Search: ")
        searching(account_name)
    
    else:
        account_delete = input("Name the Login you want to delete: ")
        result = searching(account_delete)
        if result == "Login Credential does not exist.":
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
def password_handling(password, user_name, webname, weburl):    #****Password Validation  upcoming.****
    # Confirming Password.
    # Loop for mismatched password until it matches.
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
        return("Login Credential does not exist.")
#===========================================
#Block used for deleting a particular Login 
#===========================================
def delete(account_delete):
    with open("save.json","r") as file :
        datas = json.load(file)
    print(f"Are you sure you want to delete: {account_delete}")
    delete_input = input("Enter [Y] - Yes or [N] - No: ") 
    for data in datas:
        if delete_input == "Y":
            if data == account_delete:
                datas.remove(account_delete)
                with open("save.json","w") as file:
                    json.dump(datas,file,indent="\t")
                print("Data was deleted successfully.")
        else:
            print("Data does not exists.")
    else:
        print("Delete process was cancelled.")
if __name__ == "__main__":
    main()