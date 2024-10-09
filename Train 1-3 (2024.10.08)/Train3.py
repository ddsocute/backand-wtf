# this is a Train3 project
# focus on build five function in OOP format

from Train2 import show_interface, GRADE_FULL_LIST

HEADER = ["name", "grade1", "grade2", "grade3", "total", "average"]


class Student:
    def __init__(self, name, grade1, grade2, grade3, total, average):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3
        self.total = total
        self.average = average  # 初始化單個實例


class StudentList:
    def __init__(self):
        self.students_list = []  # 儲存管理實例

    def add_student(self, name, grade1, grade2, grade3, total, average):
        student_object = Student(name, grade1, grade2, grade3, total, average)
        self.students_list.append(student_object)  # 新增實例至student_list

    def print_student_score(self):
        formatted_header = " ".join(f"{item:>10}" for item in HEADER)
        print(formatted_header)
        for each in self.students_list:
            row = [each.name, f"{each.grade1:.2f}", f"{each.grade2:.2f}", f"{each.grade3:.2f}",
                   f"{each.total:.2f}", f"{each.average:.2f}"]
            formatted_row = " ".join([f"{item:>10}" for item in row])
            print(formatted_row)

    def print_subject_score(self):
        subject_size = len(GRADE_FULL_LIST[0][1:-2])  # 先隨邊挑一行確認總共有幾個grade 再扣三（姓名 總分 平均）
        subject_list = [[] for _ in range(subject_size)]  # _表示不需要用到此循環變涼
        for each_student in self.students_list:
            for i in range(subject_size):  # 取第二到倒數第三的grade sco"re
                grade_separated = getattr(each_student, f"grade{i + 1}")  # 獲取對象屬性值
                subject_list[i].append(grade_separated)
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
        found_number = 0  # 計算找到人數
        exit_print = False
        student_name_list = []  # 建立一個放學生名字的列表
        for each_student in GRADE_FULL_LIST:
            student_name_list.append(each_student[0])
        while not exit_print:
            found_name = input("please input the student name\n")
            for name in student_name_list:
                if found_name.casefold() in name.casefold():
                    found_number += 1
                    index = student_name_list.index(name)
                    name_data = self.students_list[index]  # 找到該學生
                    values = list(name_data.__dict__.values())  # 把該學生所有值輸入列表
                    print_list.append(values)
            print(f"find {found_number} student\n")
            for found_student in print_list:
                for key, data in zip(HEADER, found_student):
                    if isinstance(data, float):  # 如果是數字先格式化到小數點第二位 後面才不會因為有名字而無法格式化
                        data = f"{data:>.2f}"
                    print(f"{key:^7} : {data:^7}")
                print(" ")
            if found_number == 0:
                print(f"You enter the wrong name")
            else:
                exit_print = True


if __name__ == "__main__":
    exit_option = False
    student = StudentList()  # 創建一個 StudentList 類的新實例
    for each_list in GRADE_FULL_LIST:
        [name_object, grade1_object, grade2_object, grade3_object, total_object, average_object] = each_list
        student.add_student(name_object, grade1_object, grade2_object, grade3_object, total_object, average_object)
    # 調用 student 實例中的add_student 將拆包後的學生資料天價到 Student_list 中
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
