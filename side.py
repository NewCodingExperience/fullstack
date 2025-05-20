# this is the functions from Codecademy
# 5/13/2025

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

# this function will set the set the local variables.
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

# this is the end of the lesson of 5/15/2025
# this is the start on 5/20/2025

# Welcome to the Carly's Clippers project.
# this are set of programs that will have calculate basic python functions.

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
# assigns the total price to 0
total_price=0

# Calculate total price of all haircuts
for price in prices:
  total_price+=price

average_price=total_price/len(prices)
# Calculate average price of haircuts and counts each item.
print("Average Haircut price:" + str(average_price))

#Reduce each price by $5 in the for loop.
new_prices=[price -5 for price in prices]
print(new_prices)

#Calculate total revenue from last week
total_revenue=0
# it will take the number of items in the list and them set a range and goes through each index.
for i in range(len(hairstyles)):
  total_revenue+=prices[i] * last_week[i]
print("Total Revenue: " + str(total_revenue))

#Calculate average daily revenue
average_daily_revenue=total_revenue/7
print(average_daily_revenue)

# Find haircuts under $30
cuts_under_30=[hairstyles[i] for i in range(len(hairstyles[i])) if new_prices[i] < 30]
print(cuts_under_30)

# this is the end of the Haircut project ----------------------------------------------

# this is the start of dictionaries"
# so for dictionaries their are key: values.
# A dictionary begins and ends with curly braces { and }.
#Each item consists of a key ("avocado toast") and a value (6).
# Each key: value pair is separated by a comma.
 
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20,"pantry":22}
num_cameras = {"backyard": 6, "garage": 2,"driveway": 1}

print(sensors)

# this is another example:
translations={"mountain":"orod","bread":"bass","friend":"mellon","horse":"roch"}
# their is the key and the value.
# so their are keys such as software design and values in a list or number.
students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"]}

# this is another example:
person = {"name": "Shuri", "age": 18, "family": ["T'Chaka", "Ramonda"]}

# this a  unhashable list:
powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}
#--- If the key can change, that hash value would not be reliable.




