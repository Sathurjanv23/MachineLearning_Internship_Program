print("--ML Student Profile--")

name = input("Enter your name : ")
age = int(input("Enter your age :"))
daily_study_hours = float(input("Enter your daily study hours "))
target_role = input("Enter your target role : ")

print("\n--Your Profile--")
print(f"\nHello, my name is : {name} ")
print(f"I am {age} years old")
print(f"I study for {daily_study_hours} hours daily")
print(f"My target role is : {target_role}")

print("\n--Data Types--")
print(f"Type of name : {type(name)}")
print(f"Type of age :{type(age)}")
print(f"Type of daily study_hours: {type(daily_study_hours)}")
print(f"Type of target_role: {type(target_role)}")

print("\n--Expected interaction--")

first_number = int(input("Enter firt number :"))
second_number = int(input("Enter second number :"))

print(f"\n The sum of {first_number} and {second_number} is :{first_number + second_number}")

