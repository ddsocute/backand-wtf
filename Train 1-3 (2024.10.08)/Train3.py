# this is a Train3 project
# focus on or five function to user


from Train1 import load_txt, TXT_PATH
from Train2 import show_interface, print_student_score, GRADE_FULL_LIST

HEADER = ["name", "grade1", "grade2", "grade3", "total", "average"]


class Student:
    def __init__(self, name, grade1, grade2, grade3, total, average):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3
        self.total = total
        self.average = average


class Student_list:
    def __init__(self):
        self.students_list = []

    def __len__(self):
        return len(self.students_list)

    def add_student(self, name, grade1, grade2, grade3, total, average):
        student = Student(name, grade1, grade2, grade3, total, average)
        self.students_list.append(student)  # 字典裡面包實例

    def print_student_score(self):
        fomated_header = " ".join(f"{item:>10}" for item in HEADER)
        print(fomated_header)
        for each in self.students_list:
            row = [each.name, f"{each.grade1:.2f}", f"{each.grade2:.2f}", f"{each.grade3:.2f}",
                   f"{each.total:.2f}", f"{each.average:.2f}"]
            formatted_row = " ".join([f"{item:>10}" for item in row])
            print(formatted_row)

    def print_subject_score(self):
        subject_size = len(GRADE_FULL_LIST[0][1:-2])  # 先隨邊挑一行確認總共有幾個grade 再扣三（姓名 總分 平均）
        subject_list = [[] for _ in range(subject_size)]
        for each_student in self.students_list:
            for i in range(subject_size):  # 取第二到倒數第三的grade sco"re
                grade_seperate = getattr(each_student, f"grade{i + 1}")
                subject_list[i].append(grade_seperate)
        for index, sum_list in enumerate(subject_list):  # 把每科列表數字起來得出每科總和
            print(f"grade{index + 1} total is: {sum(sum_list):.2f} ,"
                  f" average is: {sum(sum_list) / len(GRADE_FULL_LIST):.2f}")

    def print_students_rank(self):
        each_student_average_list = []
        each_student_name_list = []
        for each in self.students_list:
            each_student_average_list.append(each.average)
            each_student_name_list.append(each.name)
        zipped = zip(each_student_name_list, each_student_average_list)  # 裝包
        sorted_zipped = sorted(zipped, key=lambda x: x[1], reverse=True)
        sorted_names, sorted_grades = zip(*sorted_zipped)  # 解包將zip回傳的迭代器裡的元組 重組成兩個元組
        for rank, name, grade in zip(range(1, len(GRADE_FULL_LIST) + 1), sorted_names, sorted_grades):
            # 用zip一一對應排名、名字與成績在輸出
            print(f"rank{rank} is {name:^7s}  average grade is {grade:.2f}")  # 格式化輸出

    def print_name_data(self):
        print_list = []
        finded_number = 0
        exit_print = False
        student_name_list = []
        finded_name = input("please input the student name\n")
        for each_student in GRADE_FULL_LIST:
            student_name_list.append(each_student[0])  # 建立一個放學生名字的列表
        while not exit_print:
            for name in student_name_list:
                if finded_name.casefold() in name.casefold():
                    finded_number += 1
                    index = student_name_list.index(name)
                    name_data = self.students_list[index]  # 找到該學生所有資料
                    values = list(name_data.__dict__.values())
                    print_list.append(values)
            print(f"find {finded_number} student\n")
            for finded_student in print_list:
                for key, data in zip(HEADER, finded_student):
                    if isinstance(data, float):  # 如果是數字先格式化到小數點第二位 後面才不會因為有名字而無法格式化
                        data = f"{data:>.2f}"
                    print(f"{key:^7} : {data:^7}")
                print(" ")
            if finded_number == 0:
                find_name = input(f"You enter the wrong name\n"
                                  "please input the student name\n")
            else:
                exit_print = True


if __name__ == "__main__":
    exit_option = False
    student = Student_list()
    student_list_object = []
    for each_list in GRADE_FULL_LIST:
        name, grade1, grade2, grade3, total, average = each_list
        student.add_student(name, grade1, grade2, grade3, total, average)
    if __name__ == "__main__":
        while not exit_option:
            show_interface()
            option = input()
            if option == "1":
                student.print_student_score()
            elif option == "2":
                student.print_subject_score()
            elif option == "3":
                student.print_students_rank()
            elif option == "4":
                student.print_name_data()
            elif option == "5":
                print("See you next time")
                exit_option = True
            else:
                print("Wrong input!! Please enter again.")