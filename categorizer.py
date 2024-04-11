main_word = "issue"
keywords = "login", "performance", "error"


def categorizer(text):
    if main_word in text:
        for keyword in keywords:
            if keyword in text:
                return f"An issue was found. Here is the text: '{text}', and it belongs in the category: {keyword}"
        if keyword not in text:
                return f"An issue was found. Here is the text: '{text}', but it does not belong in the category"
    else:
        return "The specific issue does not fall into a category."


while True:
    user_input = input("Please enter the text you would like to search. ")

    result = categorizer(user_input)
    print(result)

    continue_search = input("Would you like to search more text? (yes/no) ").lower()
    if continue_search != 'yes':
        break


