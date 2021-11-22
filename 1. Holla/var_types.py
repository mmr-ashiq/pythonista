first_semester_gpa = 3.8
total_credit_of_first_semester = 14
favorite_subject_of_first_semester = "Computer Fundamentals"

print("My first semester GPA is:", first_semester_gpa)
print(f'Total Credits that i take in first Semester: {total_credit_of_first_semester}')
print(f'My favorite subject of first semester is: {favorite_subject_of_first_semester}\n')

second_semester_gpa = 3.5
total_credit_of_second_semester = 13
favorite_subject_of_second_semester = "Data Structures"

print("My second semester GPA is:", second_semester_gpa)
print(f'Total Credits that i take in second Semester: {total_credit_of_second_semester}')
print(f'My favorite subject of second semester is: {favorite_subject_of_second_semester}\n')

total_credit_hours_of_two_semesters = total_credit_of_first_semester + total_credit_of_second_semester

total_gpa_of_two_semesters = (first_semester_gpa * total_credit_of_first_semester + second_semester_gpa * total_credit_of_second_semester) / total_credit_hours_of_two_semesters

print(f'Total credit hours of two semesters: {total_credit_hours_of_two_semesters}')
print(f'Total GPA of two semesters: {total_gpa_of_two_semesters}')