'''lists can be changed, strings cannot be changed'''
'''example_list = [23, 12, 21, 34, 54]
example_list[3] = 14
print(example_list)'''

'''example_string = "this string cannot be altered"
try:
    example_string[1] = "word"
except:
    print("strings cannot be altered")
print(example_string)'''

'''lists can be concatenated'''
'''a = [2, 4, 6, 8]
b = [1, 3, 5, 7]
c = a + b
print(c)'''

# lists can be sliced. the code below will print 2 - 3 only because [:6] means print up to but not including 5
a = [2, 4, 6, 8]
b = [1, 3, 5, 7]
c = a + b
print(c[:6])

# adding new items to a list using .append()
new_list = ["red wine", "broccoli", "green beans"]
new_list.append("sweet corn")
new_list.append("carrot")
new_list.append("bell pepper")
print(new_list)

# knowing if an item is in a list
a = [2, 4, 6, 8]
if 11 in a:
    print("True")
else:
    print("False")