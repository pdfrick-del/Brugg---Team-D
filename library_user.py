import csv
import getpass

def load_users():
    with open("Projekt/Brugg---Team-D/Library_User_Login_data.csv", "r", newline="", encoding="utf-8") as file:
      reader = csv.DictReader(file)
      users = list(reader)
    return users


while True:
  #---Libary User Login---
  while True:
    print("Do you have a library user account?")
    print("1. YES")
    print("2. NO")

    choice = " "

    while choice != "1" and choice != "2":
      choice = input("Choose 1 or 2: ")
      if choice != "1" and choice != "2":
        print("Error; return to choice")

    if choice == "1":
      email = input("Enter email: ").strip().lower()
      password = getpass.getpass("Enter password: ", echo_char="*")

      users = load_users()

      logged_in = False

      for user in users:
        if email == user["Email"] and password == user["Password"]:
          print("Welcome", user["Username"])
          logged_in = True
          break

      else:
        print("Incorrect login credentials; return to choice")

      if logged_in:  
        break

    elif choice == "2":

      new_name = ""
      
      while True:
        new_name = input("Enter your first name and last name: ").strip().title()

        if new_name == "":
          continue

        else:
          break

      print("Choose your new user name")

      new_user_name =""

      while True:
          new_user_name = input("Enter new username: ").strip().lower()
          
          if new_user_name == "":
            continue

          with open("Projekt/Brugg---Team-D/Library_User_Login_data.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            users = list(reader)

          for user in users:
            if new_user_name == user["Username"]:
              print("Username already exists")
              print("Error; return to new user name")
              break
          
          else:
            print("Username is available")
            break

      new_password = ""

      while True:
        new_password = getpass.getpass("Enter new password. Please make sure that the password is at least 8 characters long and does not contain any spaces.: ", echo_char="*")

        if new_password == "" or len(new_password) < 8 or " " in new_password:
          print("The password does not meet the requirements.")
          continue

        else:
          break

      new_email = ""

      while True:
        new_email = input("Enter your E-Mail: ").strip().lower()

        if new_email == "" or "@" not in new_email or "." not in new_email:
          print("Invalid email address. Please try again.")
          continue

        with open("Projekt/Brugg---Team-D/Library_User_Login_data.csv", "r", newline="", encoding="utf-8") as file:
          reader = csv.DictReader(file)
          users = list(reader)

        for user in users:
          if new_email == user["Email"]:
            print("Email already exists")
            print("Error; return to new email")
            break

        else:
          print("Email is available")
          break    
      
      print("Choose your payment option.")
      print("TWINT")
      print("Bank Card")

      Payment_Option =""

      while Payment_Option != "TWINT" and Payment_Option != "BANK CARD":
        Payment_Option = input("Enter your payment option: ").strip().upper()
      
        if Payment_Option != "TWINT" and Payment_Option  != "BANK CARD":
          print("Error; return to payment option")

      if Payment_Option == "TWINT" or Payment_Option  == "BANK CARD":
        with open("Projekt/Brugg---Team-D/Library_User_Login_data.csv", "r", newline="", encoding="utf-8") as file:
          reader = csv.DictReader(file)
          users = list(reader)
          
        highest_id = 0

        for user in users:
          number = int(user["UserID"][1:])
          if number > highest_id:
            highest_id = number

        new_number = highest_id + 1
        new_user_id = f"U{new_number:03d}"

        with open("Projekt/Brugg---Team-D/Library_User_Login_data.csv", "r", newline="", encoding="utf-8") as file:
          text = file.read()

        with open("Projekt/Brugg---Team-D/Library_User_Login_data.csv", "a", newline="", encoding="utf-8") as file:
          if not text.endswith("\n") and text != "":
            file.write("\n")

          writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
          writer.writerow({
            "UserID": new_user_id,
            "Name": new_name,
            "Username": new_user_name,
            "Password": new_password,
            "Role": "Library User",
            "Email": new_email,
            "Payment_Options": Payment_Option 
          })

        print("Your account has been created; return to Log in.")

  #---Menu---
  while True:
    if logged_in == True:
      print("What do you want to do", user["Username"], "?")
      #---Placeholder Options---
      print("1. viewing account information")
      print("2. viewing fees")
      print("3. searching books")
      print("4. requesting books")
      print("5. Log out")

      choice_options = " "
        
      while choice_options != "1" and choice_options != "2" and choice_options != "3" and choice_options != "4" and choice_options != "5":
        choice_options = input("Choose 1, 2, 3, 4 or 5: ")
        
        if choice_options != "1" and choice_options != "2" and choice_options != "3" and choice_options != "4" and choice_options != "5":
          print("Error; return to options")
      
        if choice_options == "1":
          while True:
            print("User ID:", user["UserID"])
            print("Name:", user["Name"])
            print("Username:", user["Username"])
            print("Password:", "*" * len(user["Password"]))
            print("Role:", user["Role"])
            print("Email:", user["Email"])
            print("Payment Options:", user["Payment_Options"])

            print("Would you like to edit your account information?")
            print("1. Name")
            print("2. Username")
            print("3. Password")
            print("4. Email")
            print("5. Payment Options")
            print("6 No")

            choice_edit = ""

            while choice_edit != "1" and choice_edit != "2" and choice_edit != "3" and choice_edit != "4" and choice_edit != "5" and choice_edit != "6":
              choice_edit = input ("Choose 1, 2, 3, 4, 5 or 6: ")

              if choice_edit == "1":
                with open("Projekt/Brugg---Team-D/Library_User_Login_data.csv", "r", newline="", encoding="utf-8") as file:
                  reader = csv.DictReader(file)
                  users = list(reader)

                new_name = input("Enter your new name: ").strip().title()
                user["Name"] = new_name

                for account in users:
                  if account["UserID"] == user["UserID"]:
                      account["Name"] = new_name
                      break

                with open("Projekt/Brugg---Team-D/Library_User_Login_data.csv", "w", newline="", encoding="utf-8") as file:
                  writer = csv.DictWriter(file, fieldnames=users[0].keys())
                  writer.writeheader()
                  writer.writerows(users)

      #---Placeholder Options---
      if choice_options == "2" or choice_options == "3" or choice_options == "4":
        break

      if choice_options == "5":
        print("logging out; return to choice")
        break