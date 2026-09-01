print("=" *55)
print("          ML INTERNSHIP SKILLS TRACKER")
print("=" *55)

#student profile using dictionary
student ={
    "name": input("Enter your name: "),
    "university": input("Enter your university: "),
    "target_role": input("Enter your target role: ")
}

#Fixed readmap using a tuple
ml_roadmap = (
    "Python Programming",
    "Data Analysis with Pandas",
    "Data Visualization with Matplotlib and Seaborn",
    "Machine Learning with Scikit-learn",
    "Deep Learning with TensorFlow and Keras",
    "Natural Language Processing (NLP)",
    "Model Deployment and MLOps",
    "SQL and Databases",
    "Big Data and Spark"
)

#Unique skills using a set
learning_skills = set()

#Completed skills using a list
completed_skills = []

print("\n--- Student Profile ---")
print(f"Name: {student['name']}")
print(f"University: {student['university']}")
print(f"Target Role: {student['target_role']}")

print("\n--- Machine Learning Roadmap ---")

for number in range(len(ml_roadmap)):
    print(f"{number+1}. {ml_roadmap[number]}")

def show_menu():
    print("\n--- Menu ---")
    print("1. Add a skill to learning skills")
    print("2. Mark a skill as completed")
    print("3. View learning skills")
    print("4. View completed skills")
    print("5. View progress report")
    print("6. Exit")

def add_skill():
    skill = input("Enter the skill you want to learn :").strip()

    if skill == "":
        print("Skill cannot be empty. Please enter a valid skill.")
        return
    elif skill in learning_skills:
        print(f"{skill} is already in your learning skills.")

    else:
        learning_skills.add(skill)
        print(f"{skill} has been added to your learning skills.")

def view_learning_skills():
    if not learning_skills:
        print("You have not added any learning skills yet.")
    else:
        print("\n--- Learning Skills ---")
        for skill in learning_skills:
            print(f"- {skill}")
def show_progress_report():
    learning_count = len(learning_skills)
    completed_count = len(completed_skills)
    total_tracked_skills = learning_count + completed_count

    if total_tracked_skills == 0:
        progress_percentage = 0
    else:
        progress_percentage = (
            completed_count / total_tracked_skills
        ) * 100

    if progress_percentage >= 75:
        progress_status = "Excellent Progress"
        recommendation = "Start building advanced ML projects."

    elif progress_percentage >= 50:
        progress_status = "Good Progress"
        recommendation = "Continue learning and completing your remaining skills."

    elif progress_percentage >= 25:
        progress_status = "Developing"
        recommendation = "Spend more time practising your core skills."

    else:
        progress_status = "Getting Started"
        recommendation = "Start with Python and complete one skill at a time."

    print("\n" + "=" * 55)
    print("             ML SKILLS PROGRESS REPORT")
    print("=" * 55)

    print(f"Student: {student['name']}")
    print(f"University: {student['university']}")
    print(f"Target Role: {student['target_role']}")

    print(f"\nCurrently learning: {learning_count}")
    print(f"Completed skills: {completed_count}")
    print(f"Total tracked skills: {total_tracked_skills}")
    print(f"Progress percentage: {progress_percentage:.2f}%")
    print(f"Progress status: {progress_status}")
    print(f"Recommendation: {recommendation}")

    print("=" * 55)

while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_skill()

    elif choice == "2":
        skill = input("Enter the skill you have completed: ").strip()

        if skill in learning_skills:
            learning_skills.remove(skill)
            completed_skills.append(skill)
            print(f"{skill} has been marked as completed.")
        else:
            print(f"{skill} is not in your learning skills.")

    elif choice == "3":
        view_learning_skills()

    elif choice == "4":
        if not completed_skills:
            print("You have not completed any skills yet.")
        else:
            print("\n--- Completed Skills ---")

            for skill in completed_skills:
                print(f"- {skill}")

    elif choice == "5":
        show_progress_report()

    elif choice == "6":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")