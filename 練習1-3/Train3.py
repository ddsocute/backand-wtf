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
                   grade_full_list[6][4], grade_full_list[6][5])
student_list = [student1, student2, student3, student4, student5, student6]
print(student_list)
for each_student in student_list:
    student.count_subject_score(each_student)
print("grade1 total is:", grade1_total_float, " average is:", grade1_average_total,
      "\ngrade2 total is:", grade2_total_float, " average is:", grade2_average_total,
      "\ngrade3 total is:", grade3_total_float, " average is:", grade3_average_total)