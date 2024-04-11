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
           return "No keywords were found. "
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




