# this is a Train2 project
# focus on building five function to user

TXT_PATH = "/Users/ss580/Desktop/backand-wtf/練習1-3/grade.txt"

from Train1 import show_txt


class student:
    def __init__(self):
        self.name = ""
        self.grade1 = 0
        self.grade2 = 0
        self.grade3 = 0
        self.average = 0
        self.total = 0


    def count_subject_score(self, full_txt, student_object):
        self.name = full_txt[student_object][0]
        self.grade1 = full_txt[student_object][1]
        self.grade2 = full_txt[student_object][2]
        self.grade3 = full_txt[student_object][3]
        self.average = full_txt[student_object][4]
        self.total = full_txt[student_object][5]
        grade1_total_float += grade_full_list[each_person][1]
        grade2_total_float += grade_full_list[each_person][2]
        grade3_total_float += grade_full_list[each_person][3]
        grade1_average_total = round(grade1_total_float / 6, 2)
        grade2_average_total = round(grade2_total_float / 6, 2)
        grade3_average_total = round(grade3_total_float / 6, 2)




grade1_total_float = 0
grade2_total_float = 0
grade3_total_float = 0
grade1_average_total = 0
grade2_average_total = 0
grade3_average_total = 0
for each_person in range(1, 7):
    student.count_subject_score(self, show_txt, each_person)
print("grade1 total is:", grade1_total_float, " average is:", grade1_average_total,
      "\ngrade2 total is:", grade2_total_float, " average is:", grade2_average_total,
      "\ngrade3 total is:", grade3_total_float, " average is:", grade3_average_total)