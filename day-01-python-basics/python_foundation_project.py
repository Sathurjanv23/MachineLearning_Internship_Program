print("=" * 50)
print("     ML STUDY & PERFORMANCE TRACKER")
print("=" * 50)

name = input("Enter your name :")
university = input("Enter your university :")
target_role = input("Enter your target role :")

study_hours= []

print("\nEnter your study hours for the past 7 days:")

for day in range(1,8):
    hours =float(input(f"Day{day} study hours :"))
    study_hours.append(hours)

print("\n---Student Profile---")
print(f"Name :{name}")
print(f"University  :{university}")
print(f"Target Role : {target_role}")   
print(f"Study Hours for the past 7 days : {study_hours}") 


print("\n---Study Analysis---")

total_hours = sum(study_hours)
number_of_days = len(study_hours)
average_hours = total_hours / number_of_days
highest_hours = max(study_hours)
lowest_hours = min(study_hours)

print(f"Number of study days : {number_of_days}")
print(f"Total study hours : {total_hours}")
print(f"Average study hours per days : {average_hours :.2f}")
print(f"Highest study hours in a day : {highest_hours}")
print(f"Lowest study hours in a day : {lowest_hours}")

if average_hours >= 4:
    study_status = "Excellent progress! Keep up the good work."
elif average_hours >= 2:
    study_status = "Good progress! You can do even better."
else:
    study_status = "You need to dedicate more time to your studies."

print(f"\nStudy status: {study_status}")

print("\n--Test Performance Analysis--")

test_marks = []
print("Enter your marks for five python tests (out of 100):")
for test_number in range(1,6):
    marks = float(input(f"Test{test_number} marks :"))
    test_marks.append(marks)

total_marks = sum(test_marks)
average_marks = total_marks / len(test_marks)
highest_marks = max(test_marks)
lowest_marks = min(test_marks)

pass_count = 0
fail_count = 0

for marks in test_marks:
    if marks >= 50:
        pass_count += 1
    else:
        fail_count += 1

if average_marks >= 75:
    grade = "A"
elif average_marks >= 65:
    grade = "B"
elif average_marks >= 55:
    grade = "C"
elif average_marks >= 50:
    grade = "s"
else:
    grade = "F"        

print("\n---Test Performance Summary---")
print(f"Test Marks : {test_marks}")
print(f"Total marks obtained : {total_marks}")
print(f"Average marks : {average_marks :.2f}")
print(f"Highest marks : {highest_marks}")
print(f"Lowest marks : {lowest_marks}")
print(f"Number of tests passed : {pass_count}")
print(f"Number of tests failed : {fail_count}")
print(f"Grade : {grade}")


print("\n" + "=" * 50)
print("          FINAL ML PREPARATION REPORT")
print("=" * 50)

if average_hours >= 4 and average_marks >= 75 and fail_count == 0:
    preparation_status = "Excellent foundation progress"
    recommendation = "Maintain your consistency and begin advanced Python practice."

elif average_hours >= 2 and average_marks >= 65:
    preparation_status = "On track"
    recommendation = "Continue daily practice and improve weaker test areas."

elif average_marks >= 50:
    preparation_status = "Developing"
    recommendation = "Increase your study time and revise Python fundamentals."

else:
    preparation_status = "Needs improvement"
    recommendation = "Focus on fundamentals and practise consistently every day."

print(f"Student: {name}")
print(f"Target role: {target_role}")
print(f"Weekly study hours: {total_hours:.2f}")
print(f"Daily average study hours: {average_hours:.2f}")
print(f"Test average: {average_marks:.2f}")
print(f"Tests passed: {pass_count}/{len(test_marks)}")
print(f"Overall grade: {grade}")
print(f"Preparation status: {preparation_status}")
print(f"Recommendation: {recommendation}")
print("=" * 50)