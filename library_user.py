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
    new_name = input("Enter your first name and last name: ")
    new_user_name = input("Enter new username: ")
    new_password = getpass.getpass("Enter new password: ", echo_char="*")
    new_email = input("Enter your E-Mail: ")
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

      with open("Projekt/Brugg---Team-D/Library_User_Login_data.csv", "a", newline="", encoding="utf-8") as file:
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
