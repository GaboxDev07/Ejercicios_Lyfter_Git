print("--- Welcome to the Grade Calculator ---")

grade_counter = 1
approved_grades_count = 0
failed_grades_count = 0
approved_grades_average = 0.0
failed_grades_average = 0.0
overall_grades_average = 0.0
current_grade = 0.0

total_number_of_grades = int(input("Ingrese la cantidad de Notas: "))
print(total_number_of_grades)

while grade_counter <= total_number_of_grades:
    print("Ingrese la nota numero: ", grade_counter)
    current_grade = int(input("Nota: "))

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



print("El estudiante tiene esta cantidad de notas aprobadas ", approved_grades_count)
print("Este es el promedio de notas aprobadas ", approved_grades_average)
print("El estudiante tiene esta cantidad de notas desaprobadas ", failed_grades_count)
print("Este es el promedio de notas desaaprobadas ", failed_grades_average)
print("Este es el promedio de notas Total ", overall_grades_average)