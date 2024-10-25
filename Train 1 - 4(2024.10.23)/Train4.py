# this is Train4 project
# focus on build advanced five function in OOP format
# 10/25 16:29 發現可以只要 except 就好 不用特別加特定異常 除非必要

TXT_PATH = ("/Users/ss580/Desktop/backend-wtf/"
            "Train 1 - 4(2024.10.23)/Grades.txt")
HEADER = ["name", "phone", "grade1", "grade2", "grade3", "total", "average"]


# 假如 HEADER 有改記得去改第二個功能與load_txt


class Student:
    def __init__(self, name, phone, exam_history, total, average):
        self.name = name
        self.phone = phone
        self.exam_history = exam_history
        self.total = total
        self.average = average


class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)


class Function:
    @staticmethod
    def print_student_score(self_students, self_times):
        print_row = []
        # 逐個學生處理
        for student in self_students:
            if len(student.exam_history) >= self_times:  # 看考得夠不夠次
                unformatted_row = (
                        [student.name, student.phone]
                        + student.exam_history[self_times - 1]
                        + [student.total[self_times - 1],
                           student.average[self_times - 1]])
                formatted_row = []  # 將數據格式化
                for each in unformatted_row:
                    if isinstance(each, float):
                        formatted_row.append(f"{each:^15.2f}")
                    else:
                        formatted_row.append(f"{str(each):^15}")
                print_row.append("".join(formatted_row))
        if len(print_row) == 0:  # 亦即輸入的值超過考試次數 才會沒有人
            print("Wrong input! Please enter again.")
        else:
            formatted_header = "".join(f"{item:^15}" for item in HEADER)
            print_row[0:0] = [f"EXAM {self_times}", formatted_header]
            # 插入第幾次考試與排頭
            for line in print_row:
                print(line)

    @staticmethod
    def print_subject_score(self_students, self_times):
        print_row = []
        subject_name = HEADER[2:-2]
        # 索引0 1 -2 -1 分別為名字 電話 總分 平均
        # 中間剩的即為成績列
        grades = [0 * sizes for sizes in range(len(HEADER[2:-2]))]
        # 看有幾個科目就有幾個元素
        counter = 0  # 算有幾個人考
        for student in self_students:
            if len(student.exam_history) >= self_times:  # 哪位同學有考這次的試
                counter += 1
                for index, item in enumerate(
                        student.exam_history[self_times - 1]):
                    grades[index] += item
        try:
            average = [item / counter for item in grades]
            for i in range(len(subject_name)):  # 看有幾個科目就要印幾次
                print_row.append(f"{subject_name[i]:^15}{grades[i]:^15.2f}"
                                 f"{average[i]:^15.2f}")
        except ZeroDivisionError:  # 此時counter為0 代表無找到任何人 分母為零跳錯誤
            print("Wrong input! Please enter again.")
            return
        else:
            header = ["subject", "total", "average"]
            formatted_header = "".join(f"{item:^15}" for item in header)
            print_row[0:0] = [f"EXAM {self_times}", formatted_header]
            for line in print_row:
                print(line)

    @staticmethod
    def print_students_rank(self_students, self_times):
        print_row = []
        student_average = []
        student_name = []
        for student in self_students:
            if len(student.exam_history) >= self_times:  # 哪位同學有考這次的試
                student_average.append(student.average[self_times - 1])
                student_name.append(student.name)  # 取出名字與平均
        zipped = zip(student_name, student_average)  # 裝包
        sorted_zipped = sorted(zipped, key=lambda x: x[1], reverse=True)
        sorted_names, sorted_average = zip(*sorted_zipped)
        # 解包將zip回傳的迭代器裡的元組 重組成兩個元組
        for index, name in enumerate(sorted_names):
            print_row.append(
                f"{index + 1:^15}{name:^15}{sorted_average[index]:^15.2f}")

        if len(print_row) == 0:
            print("Wrong input! Please enter again.")
        else:
            header = ["rank", "name", "average"]
            formatted_header = "".join(f"{item:^15}" for item in header)
            print_row[0:0] = [f"EXAM {self_times}", formatted_header]
            for line in print_row:
                print(line)

    @staticmethod
    def print_name_data(self_students, self_times):
        # 印出標頭
        print_row = []
        partial_name = input(
            "Enter part of the student's name to search: ")
        for student in self_students:
            if len(student.exam_history) >= self_times:
                # 哪位同學有考這次的試
                if partial_name.casefold() in student.name.casefold():
                    unformatted_row = ([student.name, student.phone]
                                       + student.exam_history[self_times - 1]
                                       + [student.total[self_times - 1],
                                          student.average[self_times - 1]])
                    # 將數據格式化
                    formatted_row = []
                    for each in unformatted_row:
                        if isinstance(each, float):
                            formatted_row.append(f"{each:^15.2f}")
                        else:
                            formatted_row.append(f"{str(each):^15}")
                    print_row.append("".join(formatted_row))
        if len(print_row) == 0:
            print("You enter the wrong name or exam time.")
        else:
            formatted_header = "".join(f"{item:^15}" for item in HEADER)
            print_row[0:0] = [f"EXAM {self_times}", formatted_header]
            for line in print_row:
                print(line)


def load_txt(file_path):
    student_list = StudentList()  # 創建類別實例 []
    with open(file_path, "r") as open_txt:
        loaded_txt = open_txt.readlines()
    for line in loaded_txt:
        split_line = line.split()
        if len(split_line) == len(HEADER) - 2:
            # 假如剛好等於排頭扣總分與平均 則代表是新學生
            name = split_line[0]  # 名字在第一個
            phone = split_line[1]  # 電話在第二個
            exam_history = [float(item) for item in
                            split_line[2:]]  # 讀入的第三個後都是成績
            total = sum(exam_history)  # 計算總分
            average = total / len(exam_history)  # 計算平均分
            new_student = Student(name, phone, [], [], [])
            # 創建新實例
            student_list.add_student(new_student)
            new_student.exam_history.append(exam_history)
            new_student.total.append(total)
            new_student.average.append(average)
            current_student = new_student  # 更新當前學生

        else:
            exam_history = [float(item) for item in split_line]
            total = sum(map(float, exam_history))  # 計算總分
            average = total / len(exam_history)  # 計算平均分
            current_student.total.append(total)
            current_student.average.append(average)
            current_student.exam_history.append(exam_history)
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
            try:
                times = int(input("Which exam do you want to see? "))
                function.print_student_score(students, times)
            except ValueError:
                print("Wrong input! Please enter again.")
        elif option == "2":
            try:
                times = int(input("Which exam do you want to see? "))
                function.print_subject_score(students, times)
            except ValueError:
                print("Wrong input! Please enter again.")
        elif option == "3":
            try:
                times = int(input("Which exam do you want to see? "))
                function.print_students_rank(students, times)
            except ValueError:
                print("Wrong input! Please enter again.")
        elif option == "4":
            try:
                times = int(input("Which exam do you want to see? "))
                function.print_name_data(students, times)
            except ValueError:
                print("Wrong input! Please enter again.")
        elif option == "5":
            print("See you next time!")
            break
        else:
            print("Wrong input! Please enter again.")

