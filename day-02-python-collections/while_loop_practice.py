print("\n--- While Loop Practice ---")

counter = 1

while counter <= 5:
    print("Studying Python collections:", counter)
    counter += 1

# இது while loop-க்கு வெளியே இருக்க வேண்டும்
print("All study sessions completed!")


print("\n--- Exercise: Multiplication Table ---")

number = int(input("Enter a number to print its multiplication table: "))
multiplier = 1

while multiplier <= 10:
    result = number * multiplier
    print(f"{number} * {multiplier} = {result}")
    multiplier += 1