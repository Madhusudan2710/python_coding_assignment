def create_student_dict(students, grades):
    student_dict = {students[i]: grades[i] for i in range(len(students))}
    return student_dict

# Test with the sample input
students = ['John', 'Alice', 'Bob']
grades = [90, 85, 95]
result = create_student_dict(students, grades)
print(result) 
