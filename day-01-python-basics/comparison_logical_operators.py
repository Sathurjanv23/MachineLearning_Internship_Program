print("---Comparison and Logical Operators---")

first_number = int(input("Enter the first number :"))
second_number = int(input("Enter the second number :"))

print("Equal :",first_number == second_number)
print("Not Equal :",first_number != second_number)
print("Greater than :",first_number > second_number)
print("Less than :",first_number < second_number)
print("Greater the or Equal :",first_number >= second_number)
print("Less than or Equal :",first_number <= second_number)

print("\n--Logical Operators--")

age = 23
knows_python = True 
has_ml_experience = False

print("Age eligible and kows Python : ",age >=18 and knows_python)
print("Knows Python or has ML experience : ",knows_python or has_ml_experience)
print("Does not know Python : ",not knows_python)

print("\n--Exercise--")

marks = int(input("Enter your marks :"))
attandance = int(input("Enter your attendance percentage :"))

is_eligible = marks >=50 and attandance >=80
print(f"\nIs the student eligible for the exam :{is_eligible}")