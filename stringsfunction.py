# Product Review
# Task 1


reviews = [
   "This product is really good. I'm impressed with its quality.",
   "The performance of this product is excellent. Highly recommended!",
   "I had a bad experience with this product. It didn't meet my expectations.",
   "Poor quality product. Wouldn't recommend it to anyone.",
   "The product was average. Nothing extraordinary about it."]


keywords = ["good", "excellent", "bad", "poor", "average"]


def review_keywords(reviews, keywords):
   if len(reviews) > 0:
       word = reviews.find(keywords)
       if word > 0:
           return reviews.upper()
       else:
           print("No keywords were found. ")
   else:
       print("Please enter a review you would like to search. ")


   while True:
       review_input = input("Enter a review you would like to search ")
       word_input = input("Enter a word you would like to search for. ")


       result = review_keywords(review_input, word_input)
       print(result)


       continue_search = input("Would you like to search more review? (yes/no) ").lower()
       if continue_search != 'yes':
           break




# Task 2      
review_input = []


def postive_negative(review):
   positive_count = 0
   negative_count = 0


  
   for word in review:
       if word in positive_words:
           positive_count += 1
       elif word in negative_words:
           negative_count += 1
          
   print(f"This is positive count {positive_count}. This is negative count {negative_count}")


   while True:
       this_input = input("Enter a review you would like to search ")
       review.append(this_input)
       positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
       negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
       result = postive_negative(this_input)
       print(result)


       continue_search = input("Would you like to search more review? (yes/no) ").lower()
       if continue_search != 'yes':
           break


print(postive_negative(review_input))






# Task 3
review_new = "I had a bad experience with this product. It didn't meet my expectations."


def summary(text, length):
   if len(text) <= length:
       return text
   else:
       cut_index = text.rfind(' ', 0, length) 
       if cut_index == -1: 
           cut_index = length
       return text[:cut_index]


print(summary(review_new, 30))




# Task 1: Input Length Validator
# Write a script that checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.
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


length_checker(first_name, last_name)




# Task 2: Password Complexity Checker
# Create a function that checks the complexity of a user's password. The password must be at least 8 characters long, contain one uppercase letter, one lowercase letter, and one number. If the password does not meet these criteria, print a message explaining the complexity requirements.
password = []
def password_checker(password):
   if len(password) < 8:
       print("Error: Password must be at least 8 characters long.")
   elif len(password) >= 8:
       password.isdigit() and password.isalnum() and password.isalpha()
       print("Great password")
   elif len(password) >= 8:
       password.isalnum() is not password.isalpha() is not password.isdigit()
       print("Error: Password must contain at least one uppercase letter, one lowercase letter, and one number.")
   else:
       print("None")
      


   while True:
       password = input("Enter your password: ")
       result = password_checker(password)
       print(result)


       continue_search = input("Would you like to search more text? (yes/no) ").lower()
       if continue_search != 'yes':
           break


password_checker(password)




# Task 3: Email Formatter
# Implement a script that ensures all user email addresses are in a standard format
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


email_formatter(email)


#3
# Task 1
# Write a script that takes a user's text input and identifies if it contains one of the predefined commands (e.g., "help", "issue", "contact support"). If a command is found, print a response related to the command.
keywords = "help", "issue", "contact support"
user_input = []


def text_searcher(user_text):
   keywords = ["help", "issue", "contact support"]




   if len(user_text) > 0:
       word = user_text.find(keywords)
       if word > 0:
           print(f"The keyword {word} has been found ")
       else:
           print("No keyboards have been found. ")


   while True:
       user_input = input("Enter a the text you would like to search. ")
       user_text.append(user_input)


       result = text_searcher(user_text)
       print(result)


       continue_search = input("Would you like to search more text? (yes/no) ").lower()
       if continue_search != 'yes':
           break


print(text_searcher(user_input))






# Task 2: Issue Categorizer
# If the user's input contains the word "issue", further categorize the issue based on keywords such as "login", "performance", "error", etc. Print out the category of the issue for the support team.


main_word = "issue"
keywords = "login", "performance", "error"
text = []
user_input = []


def categorizer(text):


   for word in text:
       if len(text) > 0:
           words = text.find(main_word)
           if main_word > 0:
               main_word.find(keywords)
               if keywords > 0:
                   print(f"An issue was found. Here is the text: {text} and it belongs in this category{keywords[0]}")
               else:
                   print("The keyword can not be found. ")
           else:
               print("The specific issue does not fall into a category. ")
       else:
           print("Please enter the text you would like to search. ")
      
       while True:
           user_input = input("Please enter the text you would like to search. ")


           result = categorizer(user_input)
           print(result)


           continue_search = input("Would you like to search more text? (yes/no) ").lower()
           if continue_search != 'yes':
               break


categorizer(user_input)
