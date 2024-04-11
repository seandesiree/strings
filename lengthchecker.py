first_name = []
last_name = []


def length_checker(first_name, last_name):
   if len(first_name) >= 2 and len(last_name) >= 2:
       print(f"Your first name is, ",len(first_name), "characters long, and your last name is ",len(last_name), "characters long. ")
   else:
       print(f"Your {first_name} and {last_name} is too short. ")


while True:
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    result = length_checker(first_name, last_name)
    print(result)

    continue_search = input("Would you like to search more text? (yes/no) ").lower()
    if continue_search != 'yes':
        break

