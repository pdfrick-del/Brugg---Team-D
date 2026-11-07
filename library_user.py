import csv
import getpass

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
    user_name = input("Enter username: ")
    password = input ("Enter password: ")

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
