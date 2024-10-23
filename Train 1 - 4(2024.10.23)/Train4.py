# this is Train4 project
# focus on build advanced five function in OOP format


TXT_PATH = ("/Users/ss580/Desktop/backand-wtf/"
            "Train 1 - 4(2024.10.23)/Grades.txt")
HEADER = ["name", "phone", "grade1", "grade2", "grade3", "total", "average"]


class Student:
    def __init__(self, name, phone, exam_history):
        self.name = name
        self.phone = phone
        self.exam_history = exam_history


class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)


class Function:
    def print_student_score(self, students, times):
        print(f"EXAM {times}")
        # 印出標頭
        formatted_header = " ".join(f"{item:^15}" for item in HEADER)
        print(formatted_header)

        # 逐個學生處理
        for student in students:
            if len(student.exam_history) >= times:  # 看考得夠不夠次
                grade_list = list(map(float, student.exam_history[times - 1]))
                total = sum(grade_list)  # 計算總分
                average = total / len(grade_list)  # 計算平均分

                # 將名字、電話號碼、成績、總分、平均分等放入未格式化的行
                unformatted_row = (
                        [student.name, student.phone]
                        + grade_list
                        + [total, average])

                # 將數據格式化
                formatted_row = []
                for each in unformatted_row:
                    if isinstance(each, float):
                        formatted_row.append(f"{each:^15.2f}")
                    else:
                        formatted_row.append(f"{str(each):^15}")
                print(" ".join(formatted_row))

    def print_subject_score(self, students, times):
        print(f"EXAM{times}")
        header = ["subject", "total", "average"]
        formatted_header = "".join(f"{item:^15}" for item in header)
        print(formatted_header)
        subject_name = HEADER[2:-2]
        # 索引0 1 -2 -1 分別為名字 電話 總分 平均
        # 中間剩的即為成績列
        grades = [0, 0, 0]
        counter = 0
        for student in students:
            if len(student.exam_history) >= times:  # 哪位同學有考這次的試
                counter += 1
                for index, item in enumerate(student.exam_history[times - 1]):
                    grades[index] += float(item)

        average = [item / counter for item in grades]
        for i in range(len(subject_name)):  # 看有幾個科目就要印幾次
            print(f"{subject_name[i]:^15}{grades[i]:^15.2f}"
                  f"{average[i]:^15.2f}")

    def print_students_rank(self, students, times):
        print(f"EXAM{times}")
        header = ["rank", "name", "average"]
        formatted_header = "".join(f"{item:^15}" for item in header)
        print(formatted_header)
        subject_size = len(HEADER[2:-2])
        # 索引0 1 -2 -1 分別為名字 電話 總分 平均
        # 中間剩的即為成績列
        student_average = []
        student_name = []
        counter = 0  # 算總共有幾個人考該次考試
        for student in students:
            if len(student.exam_history) >= times:  # 哪位同學有考這次的試
                counter += 1
                student_average.append(sum(map(float,
                                               student.exam_history[
                                                   times - 1])) / subject_size)
                # 把該次成績取出轉成浮點數並除上總共有幾個科目
                student_name.append(student.name)
        zipped = zip(student_name, student_average)  # 裝包
        sorted_zipped = sorted(zipped, key=lambda x: x[1], reverse=True)
        sorted_names, sorted_grades = zip(
            *sorted_zipped)  # 解包將zip回傳的迭代器裡的元組 重組成兩個元組
        for index, name in enumerate(sorted_names):
            print(f"{index + 1:^15}{name:^15}{sorted_grades[index]:^15.2f}")

    def print_name_data(self, students, partial_name, times):
        print(f"EXAM {times}")
        # 印出標頭
        formatted_header = " ".join(f"{item:^15}" for item in HEADER)
        print(formatted_header)
        time = int(times)
        while True:
            for student in students:
                if len(student.exam_history) >= time:
                    # 哪位同學有考這次的試
                    if partial_name.casefold() in student.name.casefold():
                        grade = sum(
                            map(float, student.exam_history[time - 1]))
                        total = sum(
                            map(float, student.exam_history[time - 1]))
                        average = total / len(student.exam_history[time - 1])
                        unformatted_row = (
                                [student.name, student.phone]
                                + (student.exam_history[time - 1])
                                + [total, average])
                        # 將數據格式化
                        formatted_row = []
                        for each in unformatted_row:
                            if isinstance(each, float):
                                formatted_row.append(f"{each:^15.2f}")
                            else:
                                formatted_row.append(f"{str(each):^15}")
                        print(" ".join(formatted_row))
            break
        print("you enter the erong name")


def load_txt(file_path):
    student_list = StudentList()
    student = []
    with open(file_path, "r") as open_txt:
        loaded_txt = open_txt.readlines()
    for line in loaded_txt:
        splited_line = line.split()
        if len(splited_line) == len(HEADER) - 2:
            # 假如剛好等於排頭扣總分與平均 則代表是新學生
            name = splited_line[0]  # 名字在第一個
            phone = splited_line[1]  # 電話在第二個
            exam_history = splited_line[2:]  # 讀入的第三個後都是成績
            new_student = Student(name, phone, [])  # 創建新實例
            student_list.add_student(new_student)
            new_student.exam_history.append(exam_history)
            current_student = new_student  # 更新當前學生

        else:
            current_student.exam_history.append(splited_line)
            # 把成績丟進去同學考試紀錄中
    return student_list.students


def show_interface():
    print("""
        1. Print students' grade
        2. Print subject scores
        3. Rank students
        4. Search for name
        5. Exit
        Please choose one and enter its number:\n""")


if __name__ == "__main__":
    students = load_txt(TXT_PATH)
    function = Function()

    while True:
        show_interface()
        option = input("Enter your choice: ")
        if option == "1":
            attempt = int(input("Which exam do you want to see? "))
            function.print_student_score(students, attempt)
        elif option == "2":
            attempt = int(input("Which exam do you want to see? "))
            function.print_subject_score(students, attempt)
        elif option == "3":
            attempt = int(input("Which exam do you want to see? "))
            function.print_students_rank(students, attempt)
        elif option == "4":
            partial_name = input(
                "Enter part of the student's name to search: ")
            times = input("Which exam do you want to see? ")
            function.print_name_data(students, partial_name, times)
        elif option == "5":
            print("See you next time!")
            break
        else:
            print("Wrong input! Please enter again.")
