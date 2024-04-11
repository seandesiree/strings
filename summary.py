review_new = "I had a bad experience with this product. It didn't meet my expectations."


def summary(text, length):
   if len(text) <= length:
       return text
   else:
       cut_index = text.rfind(' ', 0, length) 
       if cut_index == -1: 
           cut_index = length
       return text[:cut_index] + "..."


print(summary(review_new, 30))
