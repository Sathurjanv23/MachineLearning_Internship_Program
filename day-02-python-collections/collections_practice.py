print("--- Python Collections ---")

skills_list = ["Python", "Git", "Python"]
skills_tuple = ("NumPy", "Pandas", "SQL")
skills_set = {"Python", "Git", "Python"}

student = {
    "name": "Sathurjan",
    "university": "University of Moratuwa",
    "target_role": "Machine Learning Engineer"
}

print("\nList:", skills_list)
print("Tuple:", skills_tuple)
print("Set:", skills_set)
print("Dictionary:", student)

skills_list.append("Machine Learning")
skills_set.add("Pandas")

student["daily_hours"] = 3
student["target_role"] = "ML Engineer"

print("\nUpdated list :",skills_list)
print("Updated set :",skills_set)
print("Updated role :",student["target_role"])
print("Updated daily hours :",student["daily_hours"])


print("\n--- Exercise ---")

project = {
    "name": "ML Study Tracker",
    "language": "Python",
    "completed": False,
    "skills": ["Python"]
}

project["skills"].append("Pandas")
project["completed"] = True
project["github"] = "https://github.com/Sathurjanv23/MachineLearning_Internship_Program"

print("Updated project:", project)