print("Welcome to list and iterable extra practice 4")


my_list_of_words = []
above_four_letters = []

print ("Enter 5 words")
for words in range(5):
    words = (input("Enter the words now: ")) 
    my_list_of_words.append(words)

for word in my_list_of_words:
    if len(word) > 4:
        above_four_letters.append(word)

print("The words with more than 4 letters are: ", above_four_letters)