''' For loop is useful for itereating through sequences of files. To open an external file, the following is done'''
#create a variable to save the opened file. Itereate through the file to get all lines and print them. 
save_here = open("external_file.txt")
for lines in save_here:
    print(lines)

# counting the lines in a file
save_here = open("external_file.txt")
count = 0
for lines in save_here:
    count = count + 1
print(count)

# reading the file and printing a certain number of characters from the file using slice[:].
# Note that print(read_file[:20]) will print up to but not including character 20
save_here = open("external_file.txt")
read_file = save_here.read()
print(read_file[:20])

# searching through a file using the .startwith() function
# any line that begins with "school" will be printed.
save_here = open("external_file.txt")
for lines in save_here:
    if lines.startswith("school"):
        print(lines)

# the code above will print the lines but with white spaces. So we need to strip those lines using the strip function
save_here = open("external_file.txt")
for lines in save_here:
    lines = lines.strip()
    if lines.startswith("school"):
        print(lines)

# try and except function: try and except functions are used to avoid the lengthy traceback error from python.
# assuming the following code contains a file that doesn't exist:

save_here = input("enter file name: ")
count = 0
try:
    open_file = open(save_here)
except:
    print("the file could not be opened", save_here)
    quit()
for lines in save_here:
    if lines.startswith("subject: "):
        count = count + 1
        print(f"there are {count} subject lines in {save_here}")

