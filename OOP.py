class Student:
    def __init__(self, name, surname, gender):
        # Reviewer.__init__(self, name, surname)
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.srgr = float()
        self.count_all = float()
        # self.courses_attached = []

    def srgr(self):
        grades_count = 0
        if not self.grades:
            return 0
        spisok = []
        for k in self.grades:
            grades_count += len(self.grades[k])
            spisok.extent(k)
        return float(sum(spisok) / max(len(spisok), 1))

    def __str__(self):
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
            self.average_rating = sum(
                map(sum, self.grades.values())) / grades_count
        res = f'Имя:{self.name}\n' \
            f'Фамилия:{self.surname}\n' \
            f'Средняя оценка за домашнее задание:{self.average_rating}\n' \
            f'Курсы в процессе обучени:{courses_in_progress_string}\n' \
            f'Завершенные курсы:{finished_courses_string}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            # return
        return self.srgr < other.srgr

    def rate_hw(self, lecturer, course, grade):
        if isinstance(
                lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        # super().__init__(name, surname)
        Mentor.__init__(self, name, surname)
        self.grades = {}
        # elf.srgr = float()

    def srgr(self):
        # grades_count = 0
        # spisok=[]
        # if not self.grades:
        #    return 0

        for k in self.grades.values():
            grades_count += len(self.grades[k])
            spisok.extent(k)
        return float(sum(spisok) / max(len(spisok), 1))

    def __str__(self):
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
            self.average_rating = sum(
                map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'
        return res

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            sc = len(other.grades)
        return len(self.grades) < sc


class Reviewer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)

    # Student.__init__(self,name,surname,gender)

    def rate_hw(self, student, course, grade):
        if isinstance(
                student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


best_lecturer_1 = Lecturer('Ivan', 'Ivanov')
best_lecturer_1.courses_attached += ['Python']
best_lecturer_2 = Lecturer('Petr', 'Petrov')
best_lecturer_2.courses_attached += ['Python']
best_lecturer_3 = Lecturer('Kruto', 'Krutov')
best_lecturer_3.courses_attached += ['Python']

cool_rewiewer_1 = Reviewer('Sammy', 'Bigger')
cool_rewiewer_1.courses_attached += ['Python']
cool_rewiewer_1.courses_attached += ['Java']
cool_rewiewer_2 = Reviewer('Milen', 'Farmer')
cool_rewiewer_2.courses_attached += ['Python']
cool_rewiewer_2.courses_attached += ['Java']
student_1 = Student('Надя', 'Болгова', 'your_gender')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']
student_2 = Student('Иван', 'Иванов', 'your_gender')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Введение в программирование']
student_3 = Student('Петр', 'Петров', 'your_gender')
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Введение в программирование']
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_2, 'Python', 5)
student_1.rate_hw(best_lecturer_2, 'Python', 7)
student_1.rate_hw(best_lecturer_2, 'Phyton', 8)
student_1.rate_hw(best_lecturer_1, 'Python', 7)
student_1.rate_hw(best_lecturer_1, 'Python', 8)
student_1.rate_hw(best_lecturer_1, 'Python', 9)
student_2.rate_hw(best_lecturer_2, 'Python', 10)
student_2.rate_hw(best_lecturer_2, 'Python', 8)
student_2.rate_hw(best_lecturer_2, 'Python', 9)
student_3.rate_hw(best_lecturer_3, 'Python', 5)
student_3.rate_hw(best_lecturer_3, 'Python', 6)
student_3.rate_hw(best_lecturer_3, 'Python', 7)
cool_rewiewer_1.rate_hw(student_1, 'Python', 8)
cool_rewiewer_1.rate_hw(student_1, 'Python', 9)
cool_rewiewer_1.rate_hw(student_1, 'Python', 10)
cool_rewiewer_2.rate_hw(student_2, 'Java', 8)
cool_rewiewer_2.rate_hw(student_2, 'Java', 7)
cool_rewiewer_2.rate_hw(student_2, 'Java', 9)
cool_rewiewer_2.rate_hw(student_3, 'Python', 8)
cool_rewiewer_2.rate_hw(student_3, 'Python', 7)
cool_rewiewer_2.rate_hw(student_3, 'Python', 9)
cool_rewiewer_2.rate_hw(student_3, 'Python', 8)
cool_rewiewer_2.rate_hw(student_3, 'Python', 7)
cool_rewiewer_2.rate_hw(student_3, 'Python', 9)

print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}\n\n{student_3}')
print()
print()
print(
    f'Перечень лекторов:\n\n{best_lecturer_1}\n\n{best_lecturer_2}\n\n{best_lecturer_3}')
print()
print()
print(f'Перечень экзаменаторов:\n\n{cool_rewiewer_1}\n\n{cool_rewiewer_2}')
print()
print()
print(f'Результат сравнения студентов(по средним оценкам за ДЗ): '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} ={student_1 > student_2}')
print()
print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{best_lecturer_1.name} {best_lecturer_1.surname} < {best_lecturer_2.name} {best_lecturer_2.surname}\n\n'
      f' = {best_lecturer_1 > best_lecturer_2}')
# print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
#       f'{best_lecturer_1.name} {best_lecturer_1.surname} < {best_lecturer_2.name} {best_lecturer_2.surname}\n\n'
#       f' = {best_lecturer_1 > best_lecturer_2}')
# print(best_lecturer_1 < best_lecturer_2)
print()
student_list = [student_1, student_2, student_3]
lecturer_list = [best_lecturer_1, best_lecturer_2, best_lecturer_3]
course_name = 'Python'


def student_rating(student_list, course_name):
    count_all = []
    for stud in student_list:
        count_all.extend(stud.grades.get(course_name, []))
        return round(float(sum(count_all) / max(len(count_all), 1)), 1)


def lecturer_rating(lecturer_list, course_name):
    count_all = []
    for stud in lecturer_list:
        count_all.extend(stud.grades.get(course_name, []))
    return round(float(sum(count_all) / max(len(count_all), 1)), 1)

print(
    f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list,course_name), 'Python'}")
print()
print(
    f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list,course_name), 'Python'}")
print()
