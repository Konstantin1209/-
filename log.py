class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)   
 
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка' 
        
    def avr_student(self):
        for avr in self.grades.values():
            avr_grades = sum(avr)/len(avr)
            return avr_grades
        
    def __str__(self):
        some_student = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {round(self.avr_student(), 2)}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"
        return some_student
    
    def __eq__(self, other):
        return self.avr_student() == other.avr_student()
    
    def __lt__(self, other):
        return self.avr_student() < other.avr_student()

    def __gt__(self, other):
        return self.avr_student() > other.avr_student()
    
    def student_ratung(list_students, course_name):
        sum_all = 0 
        count_all = 0
        for stud in list_students:
            if course_name in stud.courses_in_progress:
                sum_all += stud.avr_student()
                count_all += 1
            else:
                continue
        avr_sum_student = sum_all / count_all
        return f"Средняя оценка для всех студентов на курсе {course_name}: {avr_sum_student:.2f}"
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super(). __init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        some_reviewer = f"Имя: {self.name}\nФамилия: {self.surname}"
        return some_reviewer

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super(). __init__(name, surname)
        self.grades = {}
        
    def avr_lecturer(self):
        for avr in self.grades.values():
            avr_grades = sum(avr)/len(avr)
            return avr_grades
    
    def __str__(self):
        some_lecturer = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(self.avr_lecturer(), 2)}"
        return some_lecturer
 
    def __eq__(self, other):
        return self.avr_lecturer() == other.avr_lecturer()
    
    def __lt__(self, other):
        return self.avr_lecturer() < other.avr_lecturer()

    def __gt__(self, other):
        return self.avr_lecturer() > other.avr_lecturer()

    def lecturer_ratung(list_lecturers, course_name):
        sum_all = 0 
        count_all = 0
        for lec in list_lecturers:
            if course_name in lec.courses_attached:
                sum_all += lec.avr_lecturer()
                count_all += 1
            else:
                continue
        avr_sum_lecturers = sum_all / count_all
        return f"Средняя оценка для всех лекторов на курсе {course_name}: {avr_sum_lecturers:.2f}"    


   

reviewer1 = Reviewer('Soma', 'Bud')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Anna', 'Romanova')
reviewer2.courses_attached += ['Python']

student1 = Student('Ruoy', 'Eman', 'Man')
student1.courses_in_progress += ['Python']
student1.finished_courses += ['Python-разработчик с нуля', 'Fullstack-разработчик на Python']

student2 = Student('Mike ', 'Tyson', 'Man')
student2.courses_in_progress += ['Python']
student2.finished_courses += ['Python-разработчик с нуля', 'Fullstack-разработчик на Python']

lecturer1 = Lecturer('Some', 'Buddy')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Bob ', 'Marley')
lecturer2.courses_attached += ['Python']

student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Python', 10)

student1.rate_lecturer(lecturer2, 'Python', 10)
student1.rate_lecturer(lecturer2, 'Python', 10)
student1.rate_lecturer(lecturer2, 'Python', 10)

student2.rate_lecturer(lecturer1, 'Python', 10)
student2.rate_lecturer(lecturer1, 'Python', 10)
student2.rate_lecturer(lecturer1, 'Python', 10)

student2.rate_lecturer(lecturer2, 'Python', 5)
student2.rate_lecturer(lecturer2, 'Python', 10)
student2.rate_lecturer(lecturer2, 'Python', 10)

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 5)

reviewer1.rate_hw(student2, 'Python', 5)
reviewer1.rate_hw(student2, 'Python', 5)
reviewer1.rate_hw(student2, 'Python', 5)

reviewer2.rate_hw(student1, 'Python', 10)
reviewer2.rate_hw(student1, 'Python', 5)
reviewer2.rate_hw(student1, 'Python', 5)

reviewer2.rate_hw(student2, 'Python', 5)
reviewer2.rate_hw(student2, 'Python', 5)
reviewer2.rate_hw(student2, 'Python', 5)



print(reviewer1, "\n")
print(reviewer2, "\n")
print(student1, "\n")
print(student2, "\n")
print(lecturer1, "\n")
print(lecturer2, "\n")
print(student1 < student2, "\n")
print(student1 > student2, "\n")
print(student1 == student2, "\n")

print(lecturer1 < lecturer2, "\n")
print(lecturer1 > lecturer2, "\n")
print(lecturer1 == lecturer2, "\n")

list_students = [student1, student2]
list_lecturers = [lecturer1, lecturer2]
print(Student.student_ratung(list_students, "Python"), "\n")
print(Lecturer.lecturer_ratung(list_lecturers, "Python"), "\n")

def top_students():
    list_top = []
    for list_stud in list_students:
        students = list_stud.name,list_stud.surname, list_stud.avr_student(), list_stud.courses_in_progress
        list_top.append(students)

    for list_ in list_top:
        if list_[3] == ['Python']:
            max_value = max(list_top, key=lambda x: x[2])
        else:
            continue
    print(f"Лучший студент на курсе 'Python'\nИмя:{max_value[0]}\nФамилия: {max_value[1]}\nСредний балл: {max_value[2]}", "\n" )
    
top_students()

def top_lecturers():
    list_lecturer = []
    for list_lec in list_lecturers:
        lecturers = list_lec.name, list_lec.surname, list_lec.avr_lecturer(), list_lec.courses_attached
        list_lecturer.append(lecturers)
    
    for list_ in list_lecturer:
        if list_[3] == ['Python']:
            max_value = max(list_lecturer, key=lambda x: x[2])
        else:
            continue
    print(f"Лучший лектор на курсе 'Python'\n{max_value[0]}\nФамилия: {max_value[1]}\nСредний балл: {max_value[2]}")

top_lecturers()

