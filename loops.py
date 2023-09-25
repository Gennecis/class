#iterate through n printing each value when n - 1.
# print "n is not greater than zero anymore" once the value of n is no loger greater than zero and print the last value of n.
'''n = 5
while n > 0:
    print (n)
    n -=1
print ("n is not greater than zero anymore")
print (n)'''

'''n = 0
while True:
    if n == 3:
        break
    print(n)
    n = n + 1'''

# looping through an array to determine the largest number in the array
'''largest_num_so_far = -1
print("before ", largest_num_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_num_so_far:
        largest_num_so_far = the_num
print("the largest number is",largest_num_so_far)'''

# looping through an array to determine the smallest number in the array
'''smallest_num_so_far = 100
print("before", smallest_num_so_far)
for the_num in [10, 30, 40, 60, 90, 100, 200] :
    if the_num < smallest_num_so_far :
        smallest_num_so_far = the_num
print(smallest_num_so_far)'''

# looping through an array to count the number of items in the array
'''count = 0
array_items = [20, 10, 13, 20, 19, 20, 11, 6] 
for item in array_items:
    count = count + 1
    print(count, item)'''

# looping through an array to compute the total value of items in the array
'''total = 0
array_items = [20, 10, 13, 20, 19, 20, 11, 6] 
for item in array_items:
    total = total + item
print(total)'''

# getting the average of a given array
'''count = 0
total = 0
array_items = [9, 41, 12, 3, 74, 15]
for items in array_items:
    count +=1
    total += items
    average = total/count
print(average)'''

# finding the smallest number in an array using "None" instead of using a number
'''smallest_num = None
array_items = [9, 41, 12, 3, 74, 15]
for num in array_items:
    if smallest_num == None:
        smallest_num = num
    elif num < smallest_num:
        smallest_num == num
    print(num)
print()
print("smallest number:", smallest_num)'''

# finding the biggest number in an array using "None" instead of using a number
# use "is" for boolean values only
'''largest_num = None
array_items = [9, 41, 12, 3, 74, 15]
for num in array_items:
    if largest_num is None:
        largest_num = num
    elif num > largest_num:
        largest_num = num
    print(num)
print()
print(largest_num)'''

#using for loop to iterate through strings
'''fruit = "banana"
for index, letters in enumerate (fruit):
    print(index,letters)'''

#using for loop to count the number of times a letter appears in a string
'''fruit = "banana"
count = 0
for index, letter in enumerate(fruit):
    if letter == "a":
        count = count + 1
print(letter, "appears", count, "times")'''

#using "in" as a logical operator
fruit = "banana"
if "n" in fruit:
    print("true")
if "m" not in fruit:
    print("true")
else:
    print("false")
print("-" *50)