'''
작성일: 2026.10.13
작성자: 조영채

문제: 대학교에는 학과(Department), 교과목(Course), 학생(Student)들이 존재한다. has-a 관계를 염두에 두고 프로그래밍하기.

설계:

- 클래스:
    - Department: 학과 이름과 개설 교과목 목록을 저장한다.
        - __init__(self, name): 생성자 함수
        - add_course(name, credits): 교과목을 생성해 목록에 추가하고 반환한다.

    - Course: 교과목 이름, 학점, 수강 학생 목록을 저장한다.
        - __init__(self, name, credits): 생성자 함수 

    - Student: 학생 이름, 학번, 수강 교과목 목록을 저장한다.
        - __init__(self, name, student_id): 생성자 함수
        - enroll(course): 교과목을 수강 목록에 추가한다.
'''

class Department:
    def __init__(self, name):
        self.name = name
        self.courses = []  # 이 학과에 개설된 교과목 객체들을 저장한다.

    def add_course(self, name, credits):
        # 교과목 객체를 만들고 학과의 교과목 목록에 추가한다.
        course = Course(name, credits)
        self.courses.append(course)
        return course


class Course:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits
        self.students = []  # 이 과목을 수강하는 학생 객체들을 저장한다.


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []  # 이 학생이 수강하는 교과목 객체들을 저장한다.

    def enroll(self, course):
        # 중복 등록을 막고, 학생과 과목 양쪽의 목록에 서로를 추가한다.
        if course not in self.courses:
            self.courses.append(course)
            course.students.append(self)


def test_prog6():
    # 학과를 만들고 교과목을 개설한다.
    dept = Department("컴퓨터")
    math1 = dept.add_course("공업수학", 3)
    math2 = dept.add_course("이산수학", 2)

    # 학생을 만든 뒤 수학 과목에 등록한다.
    kim = Student("Kim", 20263414)
    kim.enroll(math1)

    # 학과의 개설 과목과 학생의 수강 과목을 출력한다.
    print(f"{dept.name}학과 개설 교과목:")
    for course in dept.courses:
        print(f"- {course.name} ({course.credits}학점)")

    # join()은 수강 과목 이름들을 쉼표와 공백으로 이어 하나의 문자열로 만든다.
    print(f"{kim.name}의 수강 교과목: {', '.join(course.name for course in kim.courses)}")
    print(f"{math1.name} 수강 학생: {', '.join(student.name for student in math1.students)}")


if __name__ == "__main__":
    test_prog6()
