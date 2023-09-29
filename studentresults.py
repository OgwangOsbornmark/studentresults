print('enter your academic details')
print('\n')
student_details = {}
size = int(input('enter the size of the dictionary: '))
for i in range(size):
    name = str(input('enter student name: '))
    Reg_number = str(input('enter stdudent registration number: '))
    age = int(input('enter student age: '))
    program = str(input('enter student program: '))
    year_of_study = int(input('enter student year of study'))
    subject = {}
    for i in range(1):
        subject1 = str(input('enter the first subject: '))
        subject2 = str(input('enter the second subject: '))
        subject3 = str(input('enter the third subject: '))
        subject4 = str(input('enter the fourth subject: '))
        subject['subject1'] = subject1
        subject['subject2'] = subject2
        subject['subject3'] = subject3
        subject['subject4'] = subject4
    scores = {}
    for i in range(1):
        marks1 = int(input('enter marks for subject1: '))
        marks2 = int(input('enter marks for subject2: '))
        marks3 = int(input('enter marks for subject3: '))
        marks4 = int(input('enter marks for subject4: '))
        scores['marks1'] = marks1
        scores['marks2'] = marks2
        scores['marks3'] = marks3
        scores['marks4'] = marks4
    grades = {} 
    for i in range(1):  
        grade1 = str(input('enter the grade for marks1: ')) 
        grade2 = str(input('enter the grade for marks2: '))
        grade3 = str(input('enter the grade for marks3: '))
        grade4 = str(input('enter the grade for marks4: '))
        grades['grade1'] = grade1
        grades['grade2'] = grade2
        grades['grade3'] = grade3
        grades['grade4'] = grade4
        student_details[Reg_number] = {
            'name': name,
            'age' : age,
            'program': program,
            'year of study' : year_of_study,
            'subjects' : subject,
            'scores' : scores,
            'grade' : grades
    }
print(student_details)  
