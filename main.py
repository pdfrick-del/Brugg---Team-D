#---User Login---

print("Are you a library user or a librarian? Please type in 1 or 2 based on your role.")
print("1. library user")
print("2. librarian")

role = " "

while role != "1" and role != "2":
  role = input("Choose 1 or 2: ")
  if role != "1" and role != "2":
    print("Error; return to user role")

if role == "1":
    import library_user

if role == "2":
   import librarian