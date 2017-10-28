phrase = "A bird in the hand..."

# The , character after our print statement means that our next print statement keeps printing on the same line.

# filter out the letter "A" from our string.

for char in phrase:
  if char == "A" or char == 'a':
    print 'X',
  else:
    print char,
