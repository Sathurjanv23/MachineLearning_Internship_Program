print("--- Python Functions ---")

# Function without parameters
def show_welcome():
    print("welcome to the ML Internship Journey!")

show_welcome()

# Function with parameters
def show_profile(name,university,target_role):
    print("\n--Student Profile--")
    print(f"Name:{name}")
    print(f"University:{university}")
    print(f"Target Role:{target_role}")
show_profile("Sathurjan","University of Moratuwa","Machine Learning Engineer"   )

# Function with return value
def calculate_daily_hours(hours_per_day,days_per_week):
    total_hours = hours_per_day*days_per_week
    return total_hours

hours_per_day = 3
days_per_week = 5

daily_hours = calculate_daily_hours(hours_per_day, days_per_week)
print(f"\nTotal study hours per week : {daily_hours}")

print("\n--Study summary--")
print(f"Hours per day : {daily_hours/days_per_week}")
print(f"Days per week : {days_per_week}")


def calculate_average(marks):
    total_marks = sum(marks)
    average_marks = total_marks/len(marks)
    return average_marks

test_marks =[75, 80, 65, 90, 70]
average_marks = calculate_average(test_marks)

print(f"\nAverage marks : {average_marks}")
