"""Define a function called purify that takes in a list of numbers, 
removes all odd numbers in the list, and returns the result"""
def purify(lst):
    res = []
    for ele in lst:
        if ele % 2 == 0:
            res.append(ele)
    return res