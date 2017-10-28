grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print grade

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

def grades_variance(grades):
    variance = 0
    for number in grades:
        variance += (grades_average(grades) - number) ** 2
    return variance / len(grades)
"""Define a function, grades_std_deviation, that takes one argument called variance.

return the result of variance ** 0.5

After the function, create a new variable called variance and store the result of calling grades_variance(grades).

Finally print the result of calling grades_std_deviation(variance)."""

def grades_std_deviation(variance):
  return variance ** 0.5

variance = grades_variance(grades)

print grades_std_deviation(variance)

#The standard deviation is the square root of the variance. 
#You can calculate the square root by raising the number to the one-half power