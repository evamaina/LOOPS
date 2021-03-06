score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
"""Define a function scrabble_score that takes a string word as input
    and returns the equivalent scrabble score for that word."""

def scrabble_score(word):
  word = word.lower()
  total = 0
  for letter in word:
    for leter in score:
      if letter == leter:
        total = total + score[leter]
  return total

  
  """Scrabble is a game where players get points by spelling words. 
  Have your function loop through the word that you are given as input
  and look up the score for each letter in the score dictionary. 
  Add the score for each letter into a total of some sort.
Remember you can use a string's .lower() method to make your string lower case!
Words are scored by adding together the point values of each individual letter 
e.g "Helix" would score 15 points due to the sum of the letters: 4 + 1 + 1 + 1 + 8."""