print("--- ML Topics ---")

topics = ["Python", "Numpy", "Pandas", "Matplotlib", "Seaborn", "Scikit-learn", "Tensorflow"]
for topic in topics:
    print("I want to Learn :", topic)


print("\n--Study Days--")

for day in range(1,6):
    print("Day", day, "of study in", topic)

print("\n--- Total Study Hours ---")

study_hours = [5, 4, 6, 3, 5]
total_hours = 0

for hours in study_hours:
    total_hours +=hours

    print("Total study hours:", total_hours)

print("\n---Exercises---")

marks = [75,45,89,50,32]
pass_count =0
fail_count=0

for mark in marks :
    if mark>=50:
        pass_count += 1
    else:
        fail_count += 1
        
print("Number of students who passed:", pass_count)
print("Number of students who failed:", fail_count)