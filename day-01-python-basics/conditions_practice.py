print("--- Student Grade Calculator ---")

marks = int(input("Enter Your marks :"))

if marks < 0 or marks >100:
    print("Invalid marks. Please enter marks between 0 and 100.")
elif marks >= 75 :
    print("You have achieved an A grade.")
elif marks >=65 :
    print("You have achieved a B grade.")
elif marks >=55 :
    print("You have achieved a C grade.")
elif marks >=35 :
    print("You have achieved a D grade.")
else :
    print("You have achieved an F grade.")


print("\n--Exercise--")

number = int(input("Enter a number :"))

if number % 2 == 0:
    print(f"{number} is an even number.")

else:
    print(f"{number} is an odd number.")