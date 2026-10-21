#---User Login---

print("Do you have an library user account?")
print("1. YES")
print("2. NO")

choice = " "

while choice != "1" and choice != "2":
  choice = input("Choose 1 or 2: ")

if choice == "1":
  user_name = input("Enter username: ")
  password = input ("Enter password: ")

elif choice == "2":
  new_user_name = input("Enter new username: ")
  new_password = input("Enter new password: ")

else:
  print("Error; return to choice")
  
