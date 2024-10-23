#檔頭 import 宣告 主程式
# this is a Train2 project
# focus on building five function to user

TXT_PATH = "/練習1-3(2024.10.04)/grade.txt"

from Train1 import show_txt
# TODO: change location


def show_interface():
    print("""-------------------------------------------------
    1. Print students' grade
    2. Print subject scores
    3. Rank students
    4. Search for name
    5. Exit
    Please choose one and enter its number:\n""")


def print_student_score():
    print(*show_txt(), sep="\n")


def print_subject_score():
    grade_full_list = show_txt()
    grade1_total_float = 0
    grade2_total_float = 0
    grade3_total_float = 0
    # grade1_average_total = 0
    # grade2_average_total = 0
    # grade3_average_total = 0
    for each_person in range(1, 7):#mmm
        grade1_total_float += grade_full_list[each_person][1]
        grade2_total_float += grade_full_list[each_person][2]
        grade3_total_float += grade_full_list[each_person][3]
        grade1_average_total = round(grade1_total_float / 6, 2)
        grade2_average_total = round(grade2_total_float / 6, 2)
        grade3_average_total = round(grade3_total_float / 6, 2)
    print("grade1 total is:", grade1_total_float, " average is:", grade1_average_total,
          "\ngrade2 total is:", grade2_total_float, " average is:", grade2_average_total,
          "\ngrade3 total is:", grade3_total_float, " average is:", grade3_average_total)


def rank_students():
    #
    eachperson_average_list = []
    eachperson_name_list = []
    grade_full_list = show_txt()
    for eachperson_data_list in range(1, 7):#mmm 寫索引即可
        eachperson_average_list.append(grade_full_list[eachperson_data_list][-1])
        eachperson_name_list.append(grade_full_list[eachperson_data_list][0])
    zipped = list(zip(eachperson_name_list, eachperson_average_list))
    sorted_zipped = sorted(zipped, key=lambda x: x[1], reverse=True)
    sorted_names, sorted_grades, = zip(*sorted_zipped)
    for rank, name, grade in zip(range(1, 7), sorted_names, sorted_grades):
        print("第", rank, "名是", name, "平均為", grade, "分")


def search_for_name():
    student_list = []
    grade_full_list = show_txt()
    findname = input("please input the student name\n")
    for each_student in range(1, 7):#mmm
        student_list.append(grade_full_list[each_student][0])
    while True:
        if findname in student_list:
            findname_index = student_list.index(findname) + 1
            print(f"名字:{grade_full_list[findname_index][0]}\n"
                  f"grade1 is:{grade_full_list[findname_index][1]}\n"
                  f"grade2 is:{grade_full_list[findname_index][2]}\n"
                  f"grade3 is:{grade_full_list[findname_index][3]}\n"
                  f"total grade is:{grade_full_list[findname_index][4]}\n"
                  f"average grade is:{grade_full_list[findname_index][5]}\n")
            break
        else:
            print("You enter the wrong name\n")
            findname = input("please input the student name\n")


if __name__ == "__main__":
    while True:  # while bool (no ()):
        show_interface()
        option = input()
        if (option == "1"): #TODO: 不用括號
            print_student_score()
        elif (option == "2"):
            print_subject_score()
        elif (option == "3"):
            rank_students()#TODO: 一致性
        elif (option == "4"):
            search_for_name()
        elif (option == "5"):
            print("See you next time")
            break
        else:
            print("Wrong input!! Please enter again.")
