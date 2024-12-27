from dataclasses import dataclass, field
from prettytable import PrettyTable

TXT_PATH = "Grades.txt"
HEADER = ["name", "phone", "grade1", "grade2", "grade3", "total", "average"]


@dataclass
class Student:
    name: str
    phone: str
    exam_history: list = field(default_factory=list)
    total: list = field(default_factory=list)
    average: list = field(default_factory=list)

    @staticmethod
    def load_txt(file_path):
        """
        從檔案載入學生資料，並回傳完整學生列表。
        """
        student_list = StudentList()  # creat StudentList instance
        with open(file_path, "r") as open_txt:
            loaded_txt = open_txt.readlines()
        for line in loaded_txt:  # read line by line
            split_line = line.split()
            if len(split_line) == len(HEADER) - 2:
                # elements of Header list ["name", "phone", "grade1",
                #   "grade2", "grade3", "total", "average"]
                # elements of split_line  ["name", "phone", "grade1",
                #   "grade2", "grade3"]
                # if numbers of element of split_line is equal header's
                #   it means this line is new student
                name = split_line[0]
                phone = split_line[1]
                new_student = Student(name=name, phone=phone)
                exam_history = [
                    float(item) for item in split_line[2:]
                ]  # 讀入的第三個後都是成績
                new_student.exam_history.append(exam_history)
                new_student.total.append(sum(exam_history))
                new_student.average.append(sum(exam_history) / len(exam_history))
                # create new object,following is example:
                #   name : Chris
                #   phone : 0926423386
                #   exam_history : [[60, 70, 80]]
                #   total:[210]
                #   average:[70]
                student_list.add_student(new_student)
                current_student = new_student  # renew current_student

            else:
                exam_history = [float(item) for item in split_line]
                current_student.exam_history.append(exam_history)
                current_student.total.append(sum(exam_history))
                current_student.average.append(sum(exam_history) / len(exam_history))
                # renew exam_history of student object
        return student_list.students


class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    @property
    def max_exam_times(self):
        max_exam_times = 0
        for student in self.students:
            current_exam_times = len(student.total)
            if max_exam_times < current_exam_times:
                max_exam_times = current_exam_times
        return max_exam_times


class StudentManagement:
    @staticmethod
    def get_student_in_exam(students, times):
        """
        得到有哪些學生參加這次考試
        """
        student_in_exam = []
        for student in students:
            if len(student.exam_history) >= times:
                student_in_exam.append(student)
        return student_in_exam

    @staticmethod
    def get_subject(student_in_exam, times):
        # Header = ["name", "phone", "grade1", "grade2", "grade3",
        #           "total", "average"]
        # header[2:-2] = ["grade1", "grade2", "grade3"] 中間剩的即為成績列
        total = [0 * sizes for sizes in range(len(HEADER[2:-2]))]
        # 看有幾個科目就有幾個元素
        for student in student_in_exam:
            for index, item in enumerate(student.exam_history[times - 1]):
                total[index] += item
        average = [item / len(student_in_exam) for item in total]
        zipped_total_average = zip(total, average)
        return zipped_total_average

    @staticmethod
    def get_student_rank(student_in_exam, times):
        student_average = []
        for student in student_in_exam:
            student_average.append(student.average[times - 1])
        # 取出物件與平均
        zipped = zip(student_in_exam, student_average)  # 裝包後排序
        sorted_zipped = sorted(zipped, key=lambda x: x[1], reverse=True)
        sorted_student, _ = zip(*sorted_zipped)
        return sorted_student  #  只傳回排完的物件

    @staticmethod
    def get_find_student(student_in_exam):
        find_student_list = []
        partial_name = input("Enter part of the student's name to search: ")
        for student in student_in_exam:
            if partial_name.casefold() in student.name.casefold():
                find_student_list.append(student)  # 找到該學生物件後加進去回傳列表
        return find_student_list

    @staticmethod
    def display_student(
        times, header, student_be_displayed, display_attribute, rank=None
    ):
        table = PrettyTable()
        table.field_names = header
        rank_count = 1
        # 逐個學生處理
        for student in student_be_displayed:
            display_row = []
            for attribute in display_attribute:
                value = getattr(student, attribute)
                if attribute == "exam_history":
                    display_gradelist = value[times - 1]
                    for display_grade in display_gradelist:
                        display_row.append(f"{display_grade:.2f}")
                elif (attribute == "total") or (attribute == "average"):
                    display_row.append(f"{value[times - 1]:.2f}")
                else:
                    display_row.append(value)
            if rank:  # 當要排名時 rank為ture 在一開始插入排名
                display_row.insert(0, rank_count)
                rank_count += 1
            table.add_row(display_row)
        for field in table.field_names:
            table.align[field] = "c"
        return table

    @staticmethod
    def display_subject(header, zipped_total_average):
        table = PrettyTable()
        table.field_names = header
        subject_name = HEADER[2:-2]
        total, average = zip(*zipped_total_average)  # 解包
        total = [f"{item:.2f}" for item in total]
        average = [f"{item:.2f}" for item in average]
        for i in range(len(subject_name)):  # 看有幾個科目就要印幾次
            table.add_row([subject_name[i], total[i], average[i]])
        for field in table.field_names:
            table.align[field] = "c"
        return table


def show_interface():
    print(
        """
        1. Print students' grade
        2. Print subject scores
        3. Rank students
        4. Search for name
        5. Exit
        Please choose one and enter its number\n"""
    )


def return_valid_number(question, boundary_mini, boundary_max):
    number = input(question)
    if number.isdigit():  # 判斷是否為數字
        number = int(number)
        if boundary_mini <= number <= boundary_max:  # 判斷是否在範圍內
            return number
        else:
            print("Wrong input! Please enter again.")
            return 0  # 不符合都回傳0
    else:
        print("Wrong input! Please enter again.")
        return 0


if __name__ == "__main__":
    students = Student.load_txt(TXT_PATH)
    student_list = StudentList()
    while True:
        show_interface()
        ask_option = "Enter your choice: "
        option = return_valid_number(ask_option, 1, 5)
        if option == 0:
            continue
        elif option == 5:
            print("See you next time!")
            break
        else:
            ask_time = "Which option do you want to see? "
            exam_time = return_valid_number(ask_time, 1, student_list.max_exam_times)
            if exam_time == 0:
                continue
            else:
                if option == 1:
                    header = HEADER
                    displayed_student_list = StudentManagement.get_student_in_exam(
                        students, exam_time
                    )
                    display_attribute_list = list(vars(students[0]).keys())
                    StudentManagement.display_student(
                        exam_time,
                        header,
                        displayed_student_list,
                        display_attribute_list,
                    )
                elif option == 2:
                    header = ["subject", "total", "average"]
                    displayed_subject_list = StudentManagement.get_subject(
                        StudentManagement.get_student_in_exam(students, exam_time),
                        exam_time,
                    )
                    StudentManagement.display_subject(header, displayed_subject_list)
                elif option == 3:
                    header = ["rank", "name", "average"]
                    displayed_student_list = StudentManagement.get_student_rank(
                        StudentManagement.get_student_in_exam(students, exam_time),
                        exam_time,
                    )
                    display_attribute_list = ["name", "average"]
                    StudentManagement.display_student(
                        exam_time,
                        header,
                        displayed_student_list,
                        display_attribute_list,
                        rank=True,
                    )
                elif option == 4:
                    header = HEADER
                    displayed_student_list = StudentManagement.get_find_student(
                        StudentManagement.get_student_in_exam(students, exam_time)
                    )
                    display_attribute_list = list(vars(students[0]).keys())
                    StudentManagement.display_student(
                        exam_time,
                        header,
                        displayed_student_list,
                        display_attribute_list,
                    )
