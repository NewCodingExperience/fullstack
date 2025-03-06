print('Hello world, from VS code')
# My first line of code.
print("Hello world!")

# Define the release and runtime integer variables below:
release_year=2025
runtime=200
rating_out_of_10=7.4
# No semicolon pls.

# Prints "500"
print(573 - 74 + 1)

# Prints "50"
print(25 * 2)


# Python wants to convert int to double and will respond to double
# Prints "2.0"
print(10 / 5)



# Define the rating_out_of_10 float variable below: 

# Define how to change Python varibles:
coffee_price = 1.50
number_of_coffees = 4

# Prints "6.0"
print(coffee_price * number_of_coffees)
# Prints "1.5"
print(coffee_price)
# Prints "4"
print(number_of_coffees)

# Updating the price 
coffee_price = 2.00

# Prints "8.0"
print(coffee_price * number_of_coffees)
# Prints "2.0"
print(coffee_price)
# Prints "4"
print(number_of_coffees)


# Power rule for Python:
# 2 to the 10th power, or 1024
print(2 ** 10)

# 8 squared, or 64
print(8 ** 2)

# 9 * 9 * 9, 9 cubed, or 729
print(9 ** 3)

# We can even perform fractional exponents
# 4 to the half power, or 2
print(4 ** 0.5)


# Modulus operator takes the reminader as the answer.
# Prints 4 because 29 / 5 is 5 with a remainder of 4
print(29 % 5)
 
# Prints 2 because 32 / 3 is 10 with a remainder of 2
print(32 % 3)
 
# Modulo by 2 returns 0 for even numbers and 1 for odd numbers
# Prints 0
print(44 % 2)

# plus equals (+=)
# adds on to the strings and numbers

hike_caption = "What an amazing time to walk through nature!"

# Almost forgot the hashtags!
hike_caption += " #nofilter"
hike_caption += " #blessed"

# This is the store description:
lovely_loveseat_description="Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price=254.00
stylish_settee_description="Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

stylish_settee_price=180.50
luxurious_lamp_description="Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

luxurious_lamp_price=52.15
sales_tax=.088

customer_one_total=0
customer_one_itemization=""
customer_one_total=stylish_settee_price
customer_one_itemization=lovely_loveseat_description
customer_one_total=stylish_settee_price+luxurious_lamp_price
customer_one_itemization=lovely_loveseat_description+luxurious_lamp_description
customer_one_tax=customer_one_total * sales_tax
customer_one_total+=sales_tax
print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)



likes_snakes = input("Do you like snakes? ")

# Practice for projects:

1 == 1     # Evaluates to True as the operands are the same 

1 != 1     # Evaluates to False as the operands are the same 
# the not makes it the opposite answer.

2 != 4     # Evaluates to True as the operands are different 

3 == 5     # Evaluates to False as the operands are different
 
'7' == 7   # Evaluates to False as the operands are different types 
# One side is a string, while other side is not!

#if is_raining:
  #print("bring an umbrella")

#if age <= 13:
  #print("Sorry, parental control required")

#  Boolean expressions for (and) ( if one is true in the statement and the other is false it is false)
(1 + 1 == 2) and (2 + 2 == 4)   # True

(1 > 9) and (5 != 6)            # False

(1 + 1 == 2) and (2 < 1)        # False

(0 == 10) and (1 + 1 == 1)      # False

# OR (or) statements if one is true and other is false, it wil be true, if both are false it's false, and both true is true.
True or (3 + 4 == 7)    # True
(1 - 1 == 0) or False   # True
(2 < 0) or True         # True
(3 == 8) or (3 > 4)     # False

# The not operator is used for boolean expressions (will keep the inverse t to f vise verse)

# Keep not in each variable:

statement_one = not (4 + 5 <= 9)


statement_two = not (8 * 2) != 20 - 4


credits = 120
gpa = 1.8

if  not (credits >= 120):
  print("You do not have enough credits to graduate.")

if not(gpa >= 2.0):
  print("Your GPA is not high enough to graduate.")

if not (credits >= 120) and not (gpa >= 2.0):
  print("You do not meet either requirement to graduate!")


grade = 86
if grade >= 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif(grade >=60):
  print("D")
else:
  print("F")

grade=68
if grade >=90:
  print("your good")
elif grade <=70:
  print("love you")

# functions are being listed:
def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station.")
  print("Take the Northbound N, Q, R, or W train 1 stop.")
  print("Get off the Times Square 42nd Street stop.")

# Call your function here:
def trip_welcome():
  # Indented code is part of the function body
  print("Welcome to Tripcademy!") 
  print("Let's get you to your destination.")

# Unindented code below is not part of the function body
print("Woah, look at the weather outside! Don't walk, take the train!")

trip_welcome()


# the trip welcome
def trip_welcome(destination):
  print("Welcome to Tripcademy!") 
  print("Looks like you're going to " + destination + " today.")

# allows for parameter to be included as a argument:
     # Your code below:
def generate_trip_instructions(location):
    print("Looks like you are planning a trip to visit " + location)
    print("You can use the public subway system to get to " + location)
generate_trip_instructions("Central Park")
generate_trip_instructions("Grand Central Station")
