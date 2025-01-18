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