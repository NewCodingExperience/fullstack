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
print(hike_caption)


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



#likes_snakes = input("Do you like snakes? ")

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

if  (credits >= 120):
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

# calculate_taxi_price(rate=0.5, discount=10, miles_to_travel=100)

destination_name = "Venkatanarasimharajuvaripeta"

# Built-in function: len()
# finds the length of it.
length_of_destination = len(destination_name)

# Built-in function: print()
print(length_of_destination)

# this will make the code run effectively with max, min,
tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

# Write your code below:
max_price=max(tshirt_price,shorts_price,mug_price,poster_price)
print(max_price)
min_price=min(tshirt_price,shorts_price,mug_price,poster_price)
print(min_price)

# depends on the index and will determine where to round it
rounded_price=round(tshirt_price,2)
print(rounded_price)


# scope of the issue, just make the program work outside of it:
# This function will print a hardcoded count of how many locations we have.
favorite_locations = "Paris, Norway, Iceland"

def print_count_locations():
  favorite_locations = "Paris, Norway, Iceland"
  print("There are 3 locations")
    
# This function will print the favorite locations
def show_favorite_locations():
  print("Your favorite locations are: " + favorite_locations())

#print_count_locations()
#show_favorite_locations()

# calls the method effectively:
def calculate_exchange_usd(us_dollars, exchange_rate):
  return us_dollars * exchange_rate

new_zealand_exchange = calculate_exchange_usd(100, 1.4)

print("100 dollars in US currency would give you " + str(new_zealand_exchange) + " New Zealand dollars")

# since it's the same type and same
def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first, second, third

most_popular1, most_popular2, most_popular3=top_tourist_locations_italy()
print(most_popular1)
print(most_popular2)
print(most_popular3)

# here id a fully coded python physics project L1:
# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 
def f_to_c(f_temp):
  c_temp=(f_temp-32)*5/9
  return c_temp

f100_in_celsius=f_to_c(100)
#print(f100_in_celsius)

def c_to_f(c_temp):
  f_temp=c_temp*(9/5) + 32
  return f_temp
c0_in_fahrenheit=c_to_f(0)
#print(c0_in_fahrenheit)

def get_force(mass,acceleration):
  return mass * acceleration
train_force=get_force(train_mass,train_acceleration)
#print(train_force)
#print("The GE train supplies" + " " + str(train_force) + " " + "Newtons of force")


def get_energy(mass,c=3*10**8):
  return mass * c**2

bomb_energy=get_energy(bomb_mass)
print("A 1kg bomb supplies" + str(bomb_energy) + "Joules")

def get_work(mass,acceleration,distance):
  return get_force(mass,acceleration) * distance

train_work=get_work(train_mass,train_acceleration,train_distance)
print(train_work)

print("The GE train does" + str(train_work) + "Joules of work over" + str(train_distance) + "meters")
# This is two hours of work and shows the orginal python content and info about python financial data.
# Day one. Here is all of the information I have learned! on 5/10/2025

## Day 2 5/14/2025
# python for loops:
board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

for game in board_games:
  print(game)
  # the code will a variable in board games and will select each one in board games

for sport in sport_games:
  print(sport)

# this is for loop using range:
promise = "I will finish the python loops module!"
for claim in range(5):
  # the range is would be 1,2,3,4,5 or index 0,1,2,3,4
  print(promise)
# this is a while loop:
# Your code below: 
countdown=10
print("Starting next loop")
while countdown >=0:
  #print(countdown)
  countdown-=1
print("We have liftoff!")


# this python while loops:
python_topics = ["variables", "control flow", "loops", "modules", "classes","School"]

#Your code below: 
length=len(python_topics)
# it will 6
index=0 # it will select each index at will be at 5.
while index < length:
  print("I am learning about" + python_topics[index])
  index+=1


# this is a infinite loop that runs each on in the list forever:
# It will go through each list forever and forever and keep copying it.
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]

# this will first of go through
# the list and each dog and will select which dog matches the list
# then it will break and stop from going any further.


dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed==dog_breed_I_want:
    print("They have the dog I want!")
    break

# this is the continue statment:
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
for age in ages:
  if age < 21:
    continue
    # this contine function will allow me to skip this part of the code and skip that fails the condition and prints what is needed!
  print(age)

# this is a doubles forloop:
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold=0
for scoop in sales_data:
  for d in scoop:
    print(d)

for location in sales_data:
  for bsaleslocation in location:
    scoops_sold+=bsaleslocation
    # add all of them and will make it go to each for loop
    # and then add all of the scoops_sold and then print
    # then print them out!
print(scoops_sold)

# this is the end of 5/14/2025

# this is the start of 5/15/2025:
# this is a list comphrensives
grades = [90, 88, 62, 76, 74, 89, 48, 57]
# it adds 10 to each number and in the grades list
scaled_grades=[num +10 for num in grades]
print(scaled_grades)


# this is a more advance comphrensive list:
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
# their is the variable for each hi in heights and goes through each.

can_ride_coaster=[ hi for hi in heights if hi > 161]
print(can_ride_coaster)






