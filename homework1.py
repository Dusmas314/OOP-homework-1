class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lc(self, lecture, course, grade):
        if isinstance(lecture, Lecture) and course in lecture.courses_attached and course in self.courses_in_progress:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'
    def avg_grade(self):
        avg = 0
        i = 0
        for num_list in self.grades.values():
            for num in num_list:
                i += 1
                avg += num
        if i != 0:
            return avg / i
        else:
            return 0
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grade()}\nКурсы в процессе изучения: {', '.join(best_student.courses_in_progress)}\nЗавершенные курсы: {', '.join(best_student.finished_courses)}"
    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return self.avg_grade() < other.avg_grade()
    def __le__(self, other):
        if not isinstance(other, Student):
            return
        return self.avg_grade() <= other.avg_grade()
    def __eq__(self, other):
        if not isinstance(other, Student):
            return
        return self.avg_grade() == other.avg_grade()
    def __ne__(self, other):
        if not isinstance(other, Student):
            return
        return self.avg_grade() != other.avg_grade()
    def __gt__(self, other):
        if not isinstance(other, Student):
            return
        return self.avg_grade() > other.avg_grade()
    def __ge__(self, other):
        if not isinstance(other, Student):
            return
        return self.avg_grade() >= other.avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecture(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def avg_grade(self):
        avg = 0
        i = 0
        for num_list in self.grades.values():
            for num in num_list:
                i += 1
                avg += num
        if i != 0:
            return avg / i
        else:
            return 0
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grade()}"
    def __lt__(self, other):
        if not isinstance(other, Lecture):
            return
        return self.avg_grade() < other.avg_grade()
    def __le__(self, other):
        if not isinstance(other, Lecture):
            return
        return self.avg_grade() <= other.avg_grade()
    def __eq__(self, other):
        if not isinstance(other, Lecture):
            return
        return self.avg_grade() == other.avg_grade()
    def __ne__(self, other):
        if not isinstance(other, Lecture):
            return
        return self.avg_grade() != other.avg_grade()
    def __gt__(self, other):
        if not isinstance(other, Lecture):
            return
        return self.avg_grade() > other.avg_grade()
    def __ge__(self, other):
        if not isinstance(other, Lecture):
            return
        return self.avg_grade() >= other.avg_grade()



class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student1 = Student('Kirill', 'Shipulin', 'your_gender')
best_student.finished_courses += ['Введение в программирование']
best_student.courses_in_progress += ['Python', 'Git']
best_student1.courses_in_progress += ['Python', 'Git']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

some_lecture = Lecture('Some', 'Buddy')
some_lecture1 = Lecture('Ivan', 'Cherepanov')
some_lecture.courses_attached += ['Python']
some_lecture1.courses_attached += ['Python']

best_student.rate_lc(some_lecture, 'Python', 10)
best_student.rate_lc(some_lecture, 'Python', 9)
best_student.rate_lc(some_lecture, 'Python', 10)

best_student.rate_lc(some_lecture1, 'Python', 10)
best_student.rate_lc(some_lecture1, 'Python', 3)
best_student.rate_lc(some_lecture1, 'Python', 10)

some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)

some_reviewer.rate_hw(best_student1, 'Python', 8)
some_reviewer.rate_hw(best_student1, 'Python', 10)
some_reviewer.rate_hw(best_student1, 'Python', 7)

student_list = [best_student, best_student1]

lecture_list = [some_lecture, some_lecture1]

def get_avg_all_hw_grade(student_list, course_name):
    i = 0
    avg = 0
    for student in student_list:
        if course_name in student.grades:
            for grade in student.grades[course_name]:
                i += 1
                avg += grade
    if i != 0:
        return avg / i
    else:
        return 0

def get_avg_all_lc_grade(lecture_list, course_name):
    i = 0
    avg = 0
    for lecture in lecture_list:
        if course_name in lecture.grades:
            for grade in lecture.grades[course_name]:
                i += 1
                avg += grade
    if i != 0:
        return avg / i
    else:
        return 0


print(some_reviewer)
print()
print(some_lecture)
print()
print(best_student)
print()
print(some_lecture > some_lecture1)
print()
print(best_student < best_student1)
print()
print(get_avg_all_hw_grade(student_list, 'Python'))
print()
print(get_avg_all_lc_grade(lecture_list, 'Python'))