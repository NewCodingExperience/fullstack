# Inroduction to lists:

ints_and_strings = [1, 2, 3, "four", "five","Police"]
sam_height_and_testscore=["Sam",67,85.5,True]

# append list for python:
append_example = [ 'This', 'is', 'an', 'example']
append_example.append('list')

print(append_example)

# this is  a example of append:
orders = ["daisies", "periwinkle"]
print(orders)
orders.append("tulips")
orders.append("roses")
print(orders)


# in python: when you create a list remember you created the list.
# for example:
list_one=[6,4,3,5,2,9]
second_list=[1,4]
final_list=list_one+second_list
print(final_list)
third_list=[2,5,6,3]+[2]
# in the list if you add 5 or 6 as a int, it will error as a type error.
#So you have to add as a list with a bracket.
print(third_list)

# this will call the particular index and if you do
# print list[index] or list[int(4/2)] and will work only for int not float

employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]
employee_four=employees[3]
print(employees[5])


# negative index example
pancake_recipe = ["eggs", "flour", "butter", "milk", "sugar", "love"]
# -6         -5         -4        -3        -2          -1  
# negative element start at the back of the list
print(pancake_recipe[-1])
# so it prints love
# Your code below:

# changes the position of someone on a list
garden_waitlist=["Jiho","Adam","Sonny","Alisha"]
garden_waitlist[1]="Calla"
print(garden_waitlist)
garden_waitlist[-1]="Alex"
print(garden_waitlist)

# this is when you can .remove method: 

# Create a list
shopping_line = ["Cole", "Kip", "Chris", "Sylvana", "Chris"]

# Remove a element
shopping_line.remove("Chris")
print(shopping_line)
# it will remove the first duplicate or delete any element

# will this function work:
# it will create a list in a list like a two array and will one outside and to many inside.
#[["ds",6],["ds",4]] 
heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64],["Vik",68]]
ages=[["Aaron",15],["Dhruti",16]]

# this is a double list:
#Your code below:
# thi
class_name_test=[["Jenny",90],["Alexus",85.5],["Sam",83],["Ellie",101.5]]
print(class_name_test)
sams_score=class_name_test[2][1]
print(sams_score)
ellies_score=class_name_test[-1][-1]
print(ellies_score)

# this is the new change:
#Your code below:
incoming_class=[["Kenny","American",9],["Tanya","Ukrainian",9],["Madison","Indian",7]]
print(incoming_class)
incoming_class[2][2]=8
print(incoming_class)
# change it to the back for elements.
incoming_class[-3][-3]="Ken"
print(incoming_class)

# Your code below: 
first_names=["Ainsley","Ben","Chani","Depak"]
print(first_names)
preferred_size=["Small", "Large", "Medium"]

preferred_size.append("Medium")
print(preferred_size)

customer_data=[["Ainsley","Small",True],["Ben","Large",False],["Chani","Medium",True],["Depak","Medium",False]]
print(customer_data)

customer_data[2][2]=False
print(customer_data)
# makes sure at that row is selected and removes false
customer_data[1].remove(False)
customer_data_final=customer_data+[["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)


