# define a function that returns a given set of numbers in descending order
# e.g 123456 to 654321
def descending_order(num):
    # get the digits as a list
    number = []
    for digit in str(num):
        number.append(digit)
    print(num)
    print(number)
    # sort the digits
    number.sort(reverse = True)
    print(number)
    # turn the list back into a number
    change_number = "".join(number)
    print(int(change_number))
    return int(change_number)

descending_order(123456)

# define a function that get the initials of a user in uppercase letters
'''def get_initials(name, force_upper):
    if force_upper:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial
first_name = input("enter your first name: ")
last_name = input("enter your last name: ")
print("your initiala are:", get_initials(first_name, True) + get_initials(last_name, True))'''
# define a function that returns the initials of a user's name
'''def return_initials(name):
    username = name[:1].upper()
    return username

firstname = input("enter first name: ")
lastname = input("enter last name: ")

first_initial = return_initials(firstname)
second_initial = return_initials(lastname)
print(first_initial, second_initial)'''

# define a function that computes a user's bmi using the formular weight/height^2
'''def bmi(weight, height):
    bmi = weight/height**2
    return bmi
# allow user to enter their data for weight and height in floating point values
input_weight = float(input("enter your weight: "))
input_height = float(input("enter your height: "))

# call the function bmi with the corresponding parameters and save it to user_bmi
user_bmi = bmi(input_weight, input_height)
# display user_bmi
print ("your BMI is", user_bmi)'''

#Write a function findNeedle() that takes an array full of junk but containing one "needle"
#After your function finds the needle it should return a message (as a string) that says:
#"found the needle at position " plus the index it found the needle, so:
#Example(Input --> Output)
#["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5"

'''def find_needle(haystack):
    for index, word in enumerate(haystack):
        if word == "needle":
            display_message = "found the" + " " + str(word) + " at position" + " " + str(index)
            return display_message
array_set = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
calling_function = find_needle(array_set)
print(calling_function)'''

'''After a hard quarter in the office you decide to get some rest on a vacation. So you will book a flight for you and your girlfriend and try to leave all the mess behind you.

You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you some good offers.

Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total.

Write a code that gives out the total amount for different days(d).'''

'''def rental_car_cost(d):
    cost_per_rent = 40
    proposed_discount_7days = 50
    proposed_discount_3days = 20
    
    if d >= 7:
        total_rent_cost = (d * cost_per_rent) - proposed_discount_7days
    elif d >= 3:
        total_rent_cost = (d * cost_per_rent) - proposed_discount_3days
    else:
        total_rent_cost = d * cost_per_rent
    return total_rent_cost

num_of_days = int(input("how many days are you renting for? "))
total_charge = rental_car_cost(num_of_days)
print(f"the total charge is ", total_charge)'''


'''Complete the square sum function so that it squares each number passed into it and then sums the results together.
For example, for [1, 2, 2] it should return 9 because 1**2 + 2**2 + 2**2 = 9'''
'''
# define the function
def square_sum(numbers):
# create an empty list    
    squared_num = []
# loop through the array "numbers" and square each of them and save the result to a variable i_square    
    for i in numbers:
        i_square = i**2
# append i_square to the empty list      
        squared_num.append(i_square)
# the list should now contain [1,4,4]. sum the values in the list and return the result        
    return sum(squared_num)

# call the defined function
array_list = [4, 2, 2]
sum_array_list = square_sum(array_list)
print(sum_array_list)'''