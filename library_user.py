import csv
import getpass

#---Libary User Login---
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
  new_password = getpass.getpass("Enter new password: ")
  new_email = input("Enter your E-Mail: ")
  print("Choose your payment option.")
  print("TWINT")
  print("Bank Card")

  Payment_Option =""

  while Payment_Option != "TWINT" and Payment_Option != "BANK CARD":
    Payment_Option = input("Enter your payment option: ").strip().upper()
  
  if Payment_Option != "TWINT" and Payment_Option  != "BANK CARD":
    print("Error; return to payment option")

  elif Payment_Option == "TWINT" or Payment_Option  == "BANK CARD":
    print("Your account has been created; return to choice")
