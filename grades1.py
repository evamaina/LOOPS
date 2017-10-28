""" define a function, grades_sum that Takes in a list of scores, 
Computes the sum of the scores and Returns the computed sum.
Call the newly created grades_sum function with the list of grades and print the result."""

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total

print grades_sum(grades)

"""To compute a rolling sum, create a variable total that's initialized to zero.
 Then, as you loop through the list of grades, add the current grade to total."""