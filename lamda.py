#Lambda functions, 
# also known as anonymous functions, are small,
# inline functions that can have any number of arguments 
# but only one expression. They are defined using 
# the lambda keyword and are typically used for short, simple operations.


# Regular function 

def square(x): 

    return x ** 2 

  

# Lambda function 

square_lambda = lambda x: x ** 2 
# lambda[arguments]:[expression]


# Lambda function to add two numbers 

add = lambda a, b: a + b 

print(add(3, 5))  # Output: 8 


# map():
# The map() function applies the given lambda function to each item in a list:
numbers = [1, 2, 3, 4, 5] 

squared = list(map(lambda x: x ** 2, numbers)) 

print(squared)  # Output: [1, 4, 9, 16, 25] 

# filter:
# The filter() function creates a new list of elements for which the given lambda function returns True:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) 

print(even_numbers)  # Output: [2, 4, 6, 8, 10] 


# map functions:

# Converting strings to integers 

str_nums = ['1', '2', '3', '4', '5'] 

int_nums = list(map(int, str_nums)) 

print(int_nums)  # Output: [1, 2, 3, 4, 5] 

# another example:
# Finding the length of strings 

words = ['apple', 'banana', 'cherry'] 

word_lengths = list(map(len, words)) 

print(word_lengths)  # Output: [5, 6, 6] 


