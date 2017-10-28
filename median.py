#Write a function called median that takes a list as an input and returns the median value of the list.

def median(lst):
    sorted_list = sorted(lst)
    if len(sorted_list) % 2 != 0:
        #odd number of elements
        index = len(sorted_list)//2 
        return sorted_list[index]
    elif len(sorted_list) % 2 == 0:
        #even no. of elements
        index_1 = len(sorted_list)/2 - 1
        index_2 = len(sorted_list)/2
        mean = (sorted_list[index_1] + sorted_list[index_2])/2.0
        return mean
   
print median([2, 4, 5, 9])


"""In order to find the median of a list with an even number of elements,
 you're going to need to find the indices of the middle two elements.

You can find the middle two elements by halving the length of the array 
to find the index of the first element, and subtracting one from the first index to find the second index.

For example, with an array of length 6 like [0, 1, 2, 3, 4, 5], 
the two middle elements that need to be averaged in order find 
the median would be 2 and 3. You get 3 by cutting the length of 
the array in half and 2 by subtracting 1 from the previous index: 3. 
You can use a similar pattern to find the middle element of an odd-length list.

Last but not least, note that (2 + 3) / 2 is not the same as (2 + 3) / 2.0! 
he former is integer division, meaning Python will try to give you an integer back.
 You'll want a float, so something like (2 + 3) / 2.0 is the way to go."""