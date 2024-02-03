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
        some_student = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avr_student()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}"
        return some_student
    
    def __eq__(self, other):
        return self.self.avr_student() == other.self.avr_student()
    
    def __lt__(self, other):
        return self.self.avr_student() < other.self.avr_student()

    def __gt__(self, other):
        return self.self.avr_student() > other.self.avr_student()


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
        some_lecturer = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avr_lecturer()}"
        return some_lecturer
 
    def __eq__(self, other):
        return self.self.avr_lecturer() == other.self.avr_lecturer()
    
    def __lt__(self, other):
        return self.self.avr_lecturer() < other.self.avr_lecturer()

    def __gt__(self, other):
        return self.self.avr_lecturer() > other.self.avr_lecturer()







best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['vd']
cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']

best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 1)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)

cool_lecturer1 = Lecturer('Some', 'Buddy')
cool_lecturer1.courses_attached += ['Python']
best_student.rate_lecturer(cool_lecturer1, 'Python', 10)
best_student.rate_lecturer(cool_lecturer1, 'Python', 8)
best_student.rate_lecturer(cool_lecturer1, 'Python', 10)


 
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.rate_hw(best_student, 'Python', 1)
cool_mentor.rate_hw(best_student, 'Python', 1)
cool_mentor.rate_hw(best_student, 'Python', 10)
print(cool_mentor)
print()
print(best_student)
print()
print(cool_lecturer)
print()
print(cool_lecturer1)