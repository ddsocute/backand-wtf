TXT_PATH = ("/Users/ss580/Desktop/backand-wtf/"
            "Train 1 - 4(2024.10.23)/Grades.txt")
HEADER = ["Name", "Phone", "Grade1", "Grade2", "Grade3", "Total", "Average"]


class Student:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.exam_history = []  # List to store multiple exam attempts


class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)


class Function:
    def print_student_score(self, students, times):
        print(f"\nExam Attempt {times}")
        print("{:^15}{:^15}{:^15}{:^15}{:^15}{:^15}{:^15}".format(*HEADER))
        for student in students:
            if times <= len(student.exam_history):
                grades = student.exam_history[times - 1]
                total = sum(grades)
                average = total / len(grades)
                row = [student.name, student.phone] + grades + [total, average]
                print("{:^15}{:^15}{:^15}{:^15}{:^15}{:^15}{:^15.2f}".format(*row))


    def print_subject_score(self, students, attempt):
        print(f"\nSubject Scores for Exam Attempt {attempt}")
        subjects = ["Grade1", "Grade2", "Grade3"]
        subject_totals = [0, 0, 0]
        student_count = 0
        for student in students:
            if attempt <= len(student.exam_history):
                grades = student.exam_history[attempt - 1]
                for i in range(len(grades)):
                    subject_totals[i] += grades[i]
                student_count += 1
        if student_count > 0:
            print("{:^15}{:^15}{:^15}".format("Subject", "Total Score", "Average Score"))
            for i in range(len(subjects)):
                total_score = subject_totals[i]
                average = total_score / student_count
                print("{:^15}{:^15}{:^15.2f}".format(subjects[i], total_score, average))
        else:
            print("No data for this exam attempt.")

    def print_students_rank(self, students, attempt):
        print(f"\nStudents Ranking for Exam Attempt {attempt}")
        ranking = []
        for student in students:
            if attempt <= len(student.exam_history):
                grades = student.exam_history[attempt - 1]
                total = sum(grades)
                ranking.append((student.name, total))
        if ranking:
            ranking.sort(key=lambda x: x[1], reverse=True)
            print("{:^5}{:^15}{:^15}".format("Rank", "Name", "Total Score"))
            for idx, (name, total) in enumerate(ranking, 1):
                print("{:^5}{:^15}{:^15}".format(idx, name, total))
        else:
            print("No students took this exam attempt.")

    def print_name_data(self, students, partial_name):
        filtered_students = [student for student in students if partial_name.lower() in student.name.lower()]
        if not filtered_students:
            print(f"No students found with name containing '{partial_name}'")
            return

        print("\nStudent Contact Information and Exam Grades")
        for student in filtered_students:
            print("{:^15}{:^15}".format("Name", student.name))
            print("{:^15}{:^15}".format("Phone", student.phone))
            print("{:^15}{:^15}{:^15}{:^15}{:^15}{:^15}".format(
                "Attempt", "Grade1", "Grade2", "Grade3", "Total", "Average"))
            for attempt_num, grades in enumerate(student.exam_history, 1):
                total = sum(grades)
                average = total / len(grades)
                print("{:^15}{:^15}{:^15}{:^15}{:^15}{:^15.2f}".format(
                    attempt_num, grades[0], grades[1], grades[2], total, average))
            print("-" * 90)

def load_students(filename):
    students = []
    current_student = None
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            if not line.startswith("\t"):  # 開頭並非縮排代表有新學生
                tokens = line.split()
                if len(tokens) >= 5:
                    name = ' '.join(tokens[:-4])  # Name may contain spaces
                    phone = tokens[-4]
                    grades = list(map(int, tokens[-3:]))
                    current_student = Student(name, phone)
                    current_student.exam_history.append(grades)
                    students.append(current_student)
                else:
                    print(f"Invalid line: {line}")
            else:
                # Additional exam attempts (indented line)
                if current_student:  # 如果為None則為false
                    grades = list(map(int, line.strip().split()))
                    current_student.exam_history.append(grades)
                else:
                    print(f"Error: No student found for additional grades: {line}")
    return students

def show_interface():
    print(f"Please select an option:\n"
          "1. Print student scores for a specific exam attempt\n"
          "2. Print subject scores for a specific exam attempt\n"
          "3. Print students ranking for a specific exam attempt\n"
          "4. Search and print student contact information and grades\n"
          "5. Exit\n")

if __name__ == "__main__":
    students = load_students(TXT_PATH)
    function = Function()

    while True:
        show_interface()
        option = input("Enter your choice: ")
        if option == "1":
            attempt = int(input("Which exam attempt do you want to see? "))
            function.print_student_score(students, attempt)
        elif option == "2":
            attempt = int(input("Which exam attempt do you want to see? "))
            function.print_subject_score(students, attempt)
        elif option == "3":
            attempt = int(input("Which exam attempt do you want to see? "))
            function.print_students_rank(students, attempt)
        elif option == "4":
            partial_name = input("Enter part of the student's name to search: ")
            function.print_name_data(students, partial_name)
        elif option == "5":
            print("See you next time!")
            break
        else:
            print("Wrong input! Please enter again.")
