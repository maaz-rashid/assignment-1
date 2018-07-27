#%%
total_marks = 500
maths = 89
english = 78
urdu = 67
physics = 88
chemisrty = 93

obtained_marks = maths + english + urdu + physics + chemisrty
#%%
def calculate_grade(percentage):
    if percentage >= 90.0:
        return 'A+'
    elif percentage >= 80.0:
        return 'A'
    elif percentage >= 70.0:
        return 'B'
    elif percentage >= 60.0:
        return 'C'
    elif percentage < 60.0:
        return 'F'

percentage = obtained_marks/total_marks * 100
grade = calculate_grade(percentage)

#%%
print(f"Your Obtained Marks are: {obtained_marks}")
print(f"Your grade is: {grade}")
print(f"Your percentage is: {percentage}")


