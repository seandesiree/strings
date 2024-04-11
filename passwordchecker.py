password = []
def password_checker(password):
   if len(password) < 8:
       print("Error: Password must be at least 8 characters long.")
   elif len(password) >= 8 and any(x.isdigit()for x in password) and any(x.isalnum()for x in password) and any(x.isalpha()for x in password):
       print("Great password")
   else:
       print("Error: Password must contain at least one uppercase letter, one lowercase letter, and one number.")

      
while True:
    password = input("Enter your password: ")
    result = password_checker(password)
    print(result)


    continue_search = input("Would you like to search more text? (yes/no) ").lower()
    if continue_search != 'yes':
        break


password_checker(password)