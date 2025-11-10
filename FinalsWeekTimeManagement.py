course = input("Enter course name: ")
exam_date = input("Enter exam date: ")
study_hours = float(input("Hours you plan to study: "))
sleep_hours = float(input("Hours of sleep per day: "))

total_days = study_hours / 8
free_hours = 24 - 8 - sleep_hours

print("\nCourse: " + course + " - Exam: " + exam_date)
print("Study time needed: " + str(round(total_days, 1)) + " full days")
print("Daily free hours: " + str(free_hours))
