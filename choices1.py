choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
  print index +1 , item


  """We don't want the user to see things listed from index 0, since this looks unnatural.
   Instead, the items should appear to start at index 1. We Modify the print statement to 
   reflect this behavior by using index + 1 instead of index alone""" 