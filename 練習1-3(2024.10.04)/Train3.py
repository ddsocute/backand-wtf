# this is a Train3 project
# focus on or five function to user

TXT_PATH = "/練習1-3(2024.10.04)/grade.txt"

from Train1 import show_txt#change location
from Train2 import show_interface, print_student_score

grade1_total_float = 0
grade2_total_float = 0
grade3_total_float = 0
grade1_average_total = 0
grade2_average_total = 0
grade3_average_total = 0
eachperson_average_list = []
eachperson_name_list = []
student_name_list = []


grade_full_list = show_txt()


class student:
    def __init__(self, name, grade1, grade2, grade3, total, average):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3
        self.average = average
        self.total = total

    def count_subject_score(self):
        global grade1_total_float, grade2_total_float, grade3_total_float, grade1_average_total \
            , grade2_average_total, grade3_average_total
        grade1_total_float += self.grade1
        grade2_total_float += self.grade2
        grade3_total_float += self.grade3
        grade1_average_total = round(grade1_total_float / 6, 2)
        grade2_average_total = round(grade2_total_float / 6, 2)
        grade3_average_total = round(grade3_total_float / 6, 2)
        return grade1_total_float, grade2_total_float, grade3_total_float, grade1_average_total \
            , grade2_average_total, grade3_average_total

    def add_ranked_students(self):
        global eachperson_average_list, eachperson_name_list
        eachperson_average_list.append(self.average)
        eachperson_name_list.append(self.name)
        return eachperson_average_list, eachperson_name_list

    def ranked_students(name_list, average_list):
        zipped = list(zip(name_list, average_list))
        sorted_zipped = sorted(zipped, key=lambda x: x[1], reverse=True)
        sorted_names, sorted_grades, = zip(*sorted_zipped)
        for rank, name, grade in zip(range(1, 7), sorted_names, sorted_grades):
            print("第", rank, "名是", name, "平均為", grade, "分")

    def search_for_name(findname):
        global findname_global
        for each_student in range(1, 7):
            student_name_list.append(grade_full_list[each_student][0])
        while True:
            if findname_global in student_name_list:
                return True
            else:
                print("You enter the wrong name\n")
                findname_global = input("please input the student name\n")

    def print_student_data(self):
        print(f"名字:{self.name}\n"
              f"grade1 is:{self.grade1}\n"
              f"grade2 is:{self.grade2}\n"
              f"grade3 is:{self.grade3}\n"
              f"total grade is:{self.total}\n"
              f"average grade is:{self.average}\n")


if __name__ == "__main__":
    student1 = student(grade_full_list[1][0], grade_full_list[1][1], grade_full_list[1][2], grade_full_list[1][3],
                       grade_full_list[1][4], grade_full_list[1][5])
    student2 = student(grade_full_list[2][0], grade_full_list[2][1], grade_full_list[2][2], grade_full_list[2][3],
                       grade_full_list[2][4], grade_full_list[2][5])
    student3 = student(grade_full_list[3][0], grade_full_list[3][1], grade_full_list[3][2], grade_full_list[3][3],
                       grade_full_list[3][4], grade_full_list[3][5])
    student4 = student(grade_full_list[4][0], grade_full_list[4][1], grade_full_list[4][2], grade_full_list[4][3],
                       grade_full_list[4][4], grade_full_list[4][5])
    student5 = student(grade_full_list[5][0], grade_full_list[5][1], grade_full_list[5][2], grade_full_list[5][3],
                       grade_full_list[5][4], grade_full_list[5][5])
    student6 = student(grade_full_list[6][0], grade_full_list[6][1], grade_full_list[6][2], grade_full_list[6][3],
                       grade_full_list[6][4], grade_full_list[6][5])#TODO:each line read
    student_list = [student1, student2, student3, student4, student5, student6]

    while True:  # while bool (no ()):
        show_interface()
        option = input()
        if (option == "1"):
            print_student_score()
        elif (option == "2"):
            # print_subject_score
            for each_student in student_list:
                student.count_subject_score(each_student)
            print("grade1 total is:", grade1_total_float, " average is:", grade1_average_total,
                  "\ngrade2 total is:", grade2_total_float, " average is:", grade2_average_total,
                  "\ngrade3 total is:", grade3_total_float, " average is:", grade3_average_total)
        elif (option == "3"):
            # rank_students()
            for each_student in student_list:
                student.add_ranked_students(each_student)
            student.ranked_students(eachperson_name_list, eachperson_average_list)
        elif (option == "4"):
            # search_for_name()
            findname_global = input("please input the student name\n")
            student_dictionary = {"Chris": student1, "Jay": student2, "Coco": student3, "Amy": student4,
                                  "Quincy": student5, "Hsiu": student6}
            while student.search_for_name(findname_global):
                student.print_student_data(student_dictionary[findname_global])
                break

        elif (option == "5"):
            print("See you next time")
            break
        else:
            print("Wrong input!! Please enter again.")
