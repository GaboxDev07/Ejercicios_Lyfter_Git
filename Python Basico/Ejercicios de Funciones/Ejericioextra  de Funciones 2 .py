print ("Welcome to the Ejercicio extra de Funciones 2")

words = input ("Enter a list of words: ")
len_of_the_word = int(input("Enter the len of the word: " ))



def words_checker(words,len_of_the_word):
    words = words.split("-")
    matching_words = []
    for word in words:
        current_len_of_the_word = len(word)
        if current_len_of_the_word > len_of_the_word:
            matching_words.append(word)
    return(matching_words)

result = words_checker(words,len_of_the_word)
print(result)








