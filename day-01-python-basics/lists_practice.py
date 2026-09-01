print("--- ML Learning Topics ---")

topics = ["Python","Numpy","Pandas","Matplotlib","Seaborn","Scikit-learn","Tensorflow"]

print("\n--Topics--")
print("All topics :" ,topics)
print("first topic :",topics[0])
print("second topic :",topics[1])
print("Last topic :",topics[-1])
print("Number of topics :",len(topics))

topics.append("Keras")
print("updated topics :",topics)

topics.remove("Seaborn")
print("topics after removal :",topics)


print("\n--Exercises--")

study_hours =[5,4,6,3,5]
print("Study hours:",study_hours)
print("Total study hours:",sum(study_hours))
print("Highest hours studied in a day:",max(study_hours))
print("Lowest hours studied in a day :",min(study_hours))
print("Average study hours :",sum(study_hours)/len(study_hours))