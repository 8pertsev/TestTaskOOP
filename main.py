from student import Student
from teacher import Teacher
from utils.field_validator import FieldValidator

command = ''
student_list = []
teacher_list = []

student_list.append(Student('Petya', 'NSK', 5554433, 5))
student_list.append(Student('Natasha', 'SPB', 5557733, 4))

teacher_list.append(Teacher('Masha', 'MSK', 124567, 1000.5))
teacher_list.append(Teacher('Vanya', 'KZN', 124533, 1100.5))

print('''
list of commands
all students - print list of all students
all teachers - print list of all teachers
add student - add new student
year income - show yearly income of chosen teacher
exit - for exit
''')

while command != 'exit':
    command = input('input command: ')

    if command == 'all students':
        for e in student_list:
            e.show_info()

    elif command == 'all teachers':
        for e in teacher_list:
            e.show_info()

    elif command == 'add student':
        name = input('name: ')
        city = input('city: ')
        phnum = input('phone number:')
        mark = input('mark: ')

        phnum = FieldValidator.validate_digit(phnum, 'Phone number')
        mark = FieldValidator.validate_digit(mark, 'Mark')

        student_list.append(Student(name, city, phnum, mark))

    elif command == 'year income':
        teacher_name = input('Input teacher name: ')
        for e in teacher_list:
            if teacher_name.lower() == e.get_name().lower():
                print(f'{e.get_name()}s yearly income is {e.show_yearly_income()}')

    else:
        print('Wrong command')







