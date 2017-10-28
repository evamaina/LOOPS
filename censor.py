"""Write a function called censor that takes two strings, text and word, as input.
 It should return the text with the word you chose replaced with asterisks.e.g censor("this hack is wack hack", "hack") 
 should return: "this **** is wack ****"  """
 

def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)

    return result

    """ you can use string.split() and 
" ".join(list)After splitting the string with string.split(), you can loop through the indices in the 
list and replace the words you are looking for with their asterisk equivalent. 
Join the list at the end to get your sentence!"""