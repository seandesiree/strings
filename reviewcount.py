review_input = []


def postive_negative(review):
    positive_count = 0
    negative_count = 0
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
    for word in review:
       if word in positive_words:
           positive_count += 1
       elif word in negative_words:
           negative_count += 1
       print(f"This is positive count {positive_count}. This is negative count {negative_count}")

while True:
    this_input = input("Enter a review you would like to search ").split()
       
    result = postive_negative(this_input)
    print(result)


    continue_search = input("Would you like to search more review? (yes/no) ").lower()
    if continue_search != 'yes':
        break


