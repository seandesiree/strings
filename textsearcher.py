keywords = "help", "issue", "contact support"
user_text = []
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


text_searcher(user_input)
