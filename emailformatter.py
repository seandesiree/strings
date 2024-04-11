
email = ""
def email_formatter(email):
   symbol_checker = email.split('@')
   if len(symbol_checker) == 2:
       print(f"Your email", email, "is properly formatted")
   else:
       print("Please format your email correctly. ")


while True:
    email = input("Enter your email address: ")
    result = email_formatter(email)
    print(result)


    continue_search = input("Would you like to search more text? (yes/no) ").lower()
    if continue_search != 'yes':
        break

