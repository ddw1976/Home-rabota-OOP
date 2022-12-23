class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = 0

    def rate_les(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) \
                and course in self.courses_in_progress \
                and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"
        sum = 0
        len = 0
        for key in lecturer.grades.keys():
            for grad in list(lecturer.grades[key]):
                sum = sum + grad
                len += 1
        lecturer.average_rating = round(sum / len, 2)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Нельзя сравнить")
            return
        return self.average_rating < other.average_rating

    def __str__(self):
        res = f"Имя: {self.name}\n" \
              f"Фамилия: {self.surname}\n" \
              f"Средняя оценка за домашние задания: {self.average_rating}\n" \
              f"Курсы в процессе изучения: {self.courses_in_progress}\n" \
              f"Завершенные курсы: {self.finished_courses}"
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_rating = 0
        self.students_list = []

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Нельзя сравнить")
            return
        return self.average_rating < other.average_rating

    def __str__(self):
        res = f"Имя: {self.name} \n" \
              f"Фамилия: {self.surname} \n" \
              f"Средняя оценка за лекции: {self.average_rating}"
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) \
                and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"
        sum = 0
        len = 0
        for key in student.grades.keys():
            for grad in list(student.grades[key]):
                sum = sum + grad
                len += 1
        student.average_rating = round(sum / len, 2)

    def __str__(self):
        res = f"Имя: {self.name}\n" \
              f"Фамилия: {self.surname}"
        return res

result = {True:'Да', False:'Нет'}
#print(result[True])

student1 = Student("Иван", "Охлобыстин", "м")
student1.finished_courses += ["SQL"]
student1.courses_in_progress += ["GIT"]
student1.courses_in_progress += ["Python"]

student2 = Student("Дмитрий", "Дюжев", "м")
student2.courses_in_progress += ["Python"]
student2.finished_courses += ["C#"]

mentor1 = Mentor("Николай", "Смирнов")
mentor2 = Mentor("Александр", "Фролов")
mentor3 = Mentor("Сергей", "Родионов")
mentor4 = Mentor("Алексей", "Иванов")

lecturer1 = Lecturer("Николай", "Смирнов")
lecturer1.courses_attached += ["Python"]
lecturer1.courses_attached += ["GIT"]

lecturer2 = Lecturer("Александр", "Фролов")
lecturer2.courses_attached += ["GIT"]

reviewer1 = Reviewer("Сергей", "Родионов")
reviewer1.courses_attached += ["Python"]

reviewer2 = Reviewer("Алексей", "Иванов")
reviewer2.courses_attached += ["GIT"]
reviewer2.courses_attached += ["Python"]

# Задание 4.Полевые испытания
student_list = [student1, student2]
lecturer_list = [lecturer1, lecturer2]


def average_rating_hw(students, courses):
    sum_course_grade = 0
    iterator = 0
    for student in students:
        for key, value in student.grades.items():
            if courses in key:
                sum_course_grade += sum(value) / len(value)
                iterator += 1
    return round(sum_course_grade / iterator, 2)


def average_rating_lesson(lecturers, courses):
    sum_course_grade = 0
    iterator = 0
    for lecturer in lecturers:
        for key, value in lecturer.grades.items():
            if courses in key:
                sum_course_grade += sum(value) / len(value)
                iterator += 1
    return round(sum_course_grade / iterator, 2)


student1.rate_les(lecturer2, "GIT", 9)
student1.rate_les(lecturer2, "GIT", 10)
student1.rate_les(lecturer1, "GIT", 8)
student1.rate_les(lecturer1, "GIT", 9)
student1.rate_les(lecturer1, "Python", 9)

student2.rate_les(lecturer1, "Python", 10)
student2.rate_les(lecturer1, "Python", 10)

reviewer2.rate_hw(student1, "Python", 10)
reviewer2.rate_hw(student1, "GIT", 8)
reviewer2.rate_hw(student1, "GIT", 10)
reviewer1.rate_hw(student1, "Python", 10)
reviewer1.rate_hw(student2, "Python", 7)
reviewer1.rate_hw(student2, "Python", 9)
reviewer1.rate_hw(student2, "Python", 8)

print("     Список студентов:")
print(f"{student1}\n")
print(f"{student2}\n")
print("---------------------------------------------------------------------------------------------")
print("     Список лекторов:")
print(f"{lecturer1}\n")
print(f"{lecturer2}\n")
print("---------------------------------------------------------------------------------------------")
print("     Список проверяющих:")
print(f"{reviewer1}\n")
print(f"{reviewer2}\n")
print("---------------------------------------------------------------------------------------------")
# Сравнение лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания:
print("     Сравнение лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания:")
print(f"Средняя оценка за дз у {student1.surname} больше, чем у {student2.surname} - {result[student2.average_rating < student1.average_rating]}")
print(f"Средняя оценка за лекции у {lecturer2.surname} меньше, чем у {lecturer1.surname} - {result[lecturer2.average_rating < lecturer1.average_rating]}\n")
print("---------------------------------------------------------------------------------------------")
# Подсчет средней оценки за курсы по дз и за леции:
print("     Подсчет средней оценки за курсы по дз и за леции:")
print(f'Средняя оценка студентов за курс GIT: {average_rating_hw(student_list, "GIT")}')
print(f'Средняя оценка студентов за курс Python: {average_rating_hw(student_list, "Python")}')
print(f'Средняя оценка лекторов за курс Python: {average_rating_lesson(lecturer_list, "Python")}')
print(f'Средняя оценка лекторов за курс GIT: {average_rating_lesson(lecturer_list, "GIT")}')

