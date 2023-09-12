'''# dictionaries are used to store items like lists but in no order

# define a dictionary
example_dict = dict()
# add items to the dictionary
example_dict["phrase_one"] = "The string '[phrase_one]' is used to tag this item"
example_dict["phrase_two"] = "We can search for items in the dictionary using their lookup tag. Here the lookup tag is 'phrase_two'"
# search items in the dictionary using their lookup tag
print(example_dict["phrase_two"])
example_dict["phrase_one"] = "We can modify items in the dictionary. Here we modified 'phrase_one'"
print(example_dict["phrase_one"])
print(example_dict)

# knowing how many times an item appears in the dictionary
make_dict = dict()
names = ["wale", "yetunde", "lekan", "yetunde", "wale"]
for name in names:
    if name not in make_dict:
        make_dict[name] = 1
    else:
        make_dict[name] = make_dict[name] + 1
print(make_dict)

# knowing how many times an item appears in the dictionary method 2
dict_list = dict()
names_of_people = ["pete edochie", "jim iyke", "kenneth okonkwo", "ramsey noah", "pete edochie", "jim iyke"]
for name in names_of_people:
    dict_list[name] = dict_list.get(name, 0) + 1
print(dict_list)

# getting the keys and values of a dictionary at once.
# the first line of the code below is another way to create a dictionary.
participants = {"Toliver":23, "Ross":22, "Wayne":24, "Cole":28, "kendrick":28}
for artistes, appearance in participants.items():
    print(artistes,appearance)
# look up a single key's value
print(participants["Toliver"])'''

# finding the biggest value alongside it's key in a dictionary
biggest_value = None
key_with_biggest_value = None
participants = {"Toliver":23, "Ross":22, "Wayne":24, "Cole":28, "kendrick":28, "Dr. Dre":39}
for artiste, appearance in participants.items():
    if biggest_value is None or appearance > biggest_value:
        biggest_value = appearance
        key_with_biggest_value = artiste
print(key_with_biggest_value, biggest_value)