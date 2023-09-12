#replacing letters in strings using .replace()
'''place = "obeokuto"
refined_place = place.replace('o', 'a')
print(refined_place)'''

'''full_name = "David Crambell"
ch_full_name = full_name.replace("David Crambell", "John Snow")
print(ch_full_name)'''

# removing white spaces from strings using .strip()
# striping spaces off the right-end
'''full_name = " David Crambell "
ch_full_name = full_name.rstrip()
print(ch_full_name)'''

# striping spaces off the left-end
'''full_name = " David Crambell "
ch_full_name = full_name.lstrip()
print(ch_full_name)'''

# striping spaces off both-end
'''full_name = " David Crambell "
ch_full_name = full_name.strip()
print(ch_full_name)'''

# splitting strings into list
string_variable = "this string is to be splitted"
string_splitting = string_variable.split()
print(string_splitting)
print(len(string_splitting))