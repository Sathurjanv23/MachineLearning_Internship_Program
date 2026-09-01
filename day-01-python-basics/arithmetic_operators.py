print("--Arithmetic Calculations--")

first_number = int(input("Enter the first number :"))
second_number = int(input("Enter the second number "))

print("\n--Results--")
print(f"The Addition of {first_number} and {second_number} is : {first_number + second_number}")
print(f"The subtraction of {first_number} and {second_number} is : {first_number - second_number}")
print(f"The multiplication of {first_number} and {second_number} is : {first_number * second_number}")
print(f"The division of {first_number} and {second_number} is : {first_number / second_number}")  
print(f"The Floor Division of {first_number} and {second_number} is : {first_number // second_number}")
print(f"The Remainder of {first_number} and {second_number} is :{first_number % second_number}")
print(f"The Power of {first_number} and {second_number} is : {first_number ** second_number}")  


print("\n--Exercise--")

study_hours = int(input("Enter your daily study hours :"))
study__days = int(input("Enter the number of days you want to study :"))
total_weekly_study_hours = study_hours * study__days

print(f"\nThe total weekly study hours is :{total_weekly_study_hours}")