# define a function that computes a user's bmi using the formular weight/height^2
def bmi(weight, height):
    bmi = weight/height**2
    return bmi
# allow user to enter their data for weight and height in floating point values
input_weight = float(input("enter your weight: "))
input_height = float(input("enter your height: "))

# call the function bmi with the corresponding parameters and save it to user_bmi
user_bmi = bmi(input_weight, input_height)
# display user_bmi
print ("your BMI is", user_bmi)
