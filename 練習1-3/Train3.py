# this is a Train3 project
# focus on or five function to user

TXT_PATH = "/Users/ss580/Desktop/backand-wtf/練習1-3/grade.txt"

from Train1 import show_txt

grade1_total_float = 0
grade2_total_float = 0
grade3_total_float = 0
grade1_average_total = 0
grade2_average_total = 0
grade3_average_total = 0

class student:
    def __init__(self, name, grade1, grade2, grade3, total, average):
        self.name = ""
        self.grade1 = 0
        self.grade2 = 0
        self.grade3 = 0
        self.average = 0
        self.total = 0

    def count_subject_score(self, full_txt, student_object):
        grade_full_list = full_txt
        self.grade1 = grade_full_list[student_object][1]
        self.grade2 = grade_full_list[student_object][2]
        self.grade3 = grade_full_list[student_object][3]
        grade1_total_float += self.grade1
        grade2_total_float += self.grade1
        grade3_total_float += self.grade1
        grade1_average_total = round(grade1_total_float / 6, 2)
        grade2_average_total = round(grade2_total_float / 6, 2)
        grade3_average_total = round(grade3_total_float / 6, 2)



student1 = student(show_txt[1][0], show_txt[1][1], show_txt[1][2], show_txt[1][3],
                   show_txt[1][4], show_txt[1][5], show_txt[1][6])
student2 = student(show_txt[2][0], show_txt[2][1], show_txt[2][2], show_txt[2][3],
                   show_txt[2][4], show_txt[2][5], show_txt[2][6])
student3 = student(show_txt[3][0], show_txt[3][1], show_txt[3][2], show_txt[3][3],
                   show_txt[3][4], show_txt[3][5], show_txt[3][6])
student4 = student(show_txt[4][0], show_txt[4][1], show_txt[4][2], show_txt[4][3],
                   show_txt[4][4], show_txt[4][5], show_txt[4][6])
student5 = student(show_txt[5][0], show_txt[5][1], show_txt[5][2], show_txt[5][3],
                   show_txt[5][4], show_txt[5][5], show_txt[5][6])
student6 = student(show_txt[6][0], show_txt[6][1], show_txt[6][2], show_txt[6][3],
                   show_txt[6][4], show_txt[6][5], show_txt[6][6])
# print("grade1 total is:", grade1_total_float, " average is:", grade1_average_total,
#       "\ngrade2 total is:", grade2_total_float, " average is:", grade2_average_total,
#       "\ngrade3 total is:", grade3_total_float, " average is:", grade3_average_total)
