print("--- Welcome to the Grade Calculator ---")

grade_counter = 1
approved_grades_count = 0
failed_grades_count = 0
approved_grades_average = 0.0
failed_grades_average = 0.0
overall_grades_average = 0.0
current_grade = 0.0

total_number_of_grades = int(input("Enter the total number of grades: "))
print(total_number_of_grades)

while grade_counter <= total_number_of_grades:
    print("Enter grade number:", grade_counter)
    current_grade = int(input("Grade: "))

    if current_grade < 70:
        failed_grades_count = failed_grades_count + 1
        failed_grades_average = failed_grades_average + current_grade
    elif current_grade >= 70:
        approved_grades_count = approved_grades_count + 1
        approved_grades_average = approved_grades_average + current_grade
        overall_grades_average = overall_grades_average + (current_grade / total_number_of_grades)

    grade_counter = grade_counter + 1

if failed_grades_count > 0:
    failed_grades_average = failed_grades_average / failed_grades_count
else:
    failed_grades_count = 0

if approved_grades_count > 0:
    approved_grades_average = approved_grades_average / approved_grades_count
else:
    approved_grades_count = 0

print("The student has this number of passing grades:", approved_grades_count)
print("Average of passing grades:", approved_grades_average)
print("The student has this number of failing grades:", failed_grades_count)
print("Average of failing grades:", failed_grades_average)
print("Overall grade average:", overall_grades_average)