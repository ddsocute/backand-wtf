# this is a Train2 project
# focus on building five function to user

from Train1 import load_txt, print_txt, TXT_PATH

GRADE_FULL_LIST = load_txt(TXT_PATH)  # load data  write in main function


def show_interface():
    print("""-------------------------------------------------
    1. Print students' grade
    2. Print subject scores
    3. Rank students
    4. Search for name
    5. Exit
    Please choose one and enter its number:\n""")


def print_student_score():
    """
    print grades list like train1
    :return: formatted total grades list(contain total and average)
    """
    txt_not_formated = load_txt(TXT_PATH)
    print_txt(txt_not_formated)


def print_subject_score():
    subject_size = len(GRADE_FULL_LIST[0][1:-2])
    # [0] present first row in grades list
    # [1:-2] present total column exclude name, total, average
    subject_list = [[subject for subject in row[1:-2]]
                    for row in GRADE_FULL_LIST]
    subject_total_list = list(zip(*subject_list))
    # build a list to place each student's subject score
    for index, sum_list in enumerate(subject_total_list):
        # 把每科列表數字起來得出每科總和
        total = sum(sum_list)
        average = total / len(subject_total_list)
        print(f"grade{index + 1} total is: {total:.2f} ,"
              f" average is: {average:.2f}")


def print_students_rank():
    each_student_average_list = []
    each_student_name_list = []
    for each_student_data_list in GRADE_FULL_LIST:
        each_student_average_list.append(each_student_data_list[-1])
        each_student_name_list.append(each_student_data_list[0])
    zipped = zip(each_student_name_list, each_student_average_list)  # 裝包
    sorted_zipped = sorted(zipped, key=lambda x: x[1], reverse=True)
    # zipped.sort()  # this line do not return anything.

    sorted_names, sorted_grades = zip(
        *sorted_zipped)  # 解包將zip回傳的迭代器裡的元組 重組成兩個元組
    for i in range(1, len(GRADE_FULL_LIST) + 1):
        rank, name, grade = i, sorted_names[i - 1], sorted_grades[i - 1]
        print(
            f"rank{rank} is {name:^7}  average grade is {grade:.2f}")
        # 格式化輸出


def print_name_data():
    exit_print = False
    student_name_list = []
    head_line = ["name", "grade1", "grade2", "grade3", "total", "average"]
    find_name = input("please input the student name\n")
    for each_student in GRADE_FULL_LIST:
        student_name_list.append(each_student[0])  # 建立一個放學生名字的列表
    while True:
        # TODO: for-loop
        for each_student in GRADE_FULL_LIST:
            if find_name == each_student[0]:
                for index, data in enumerate(each_student):
                    if isinstance(data, float):
                        # 如果是數字先格式化到小數點第二位
                        # 後面才不會因為有名字而無法格式化
                        data = f"{data:>.2f}"
                    print(f"{head_line[index]:^7} : {data:^7}")
                break
        else:
            find_name = input(f"You enter the wrong name\n"
                              "please input the student name\n")
            continue
        break

if __name__ == "__main__":
    exit_option = False
    while not exit_option:
        show_interface()
        option = input()
        if option == "1":
            print_student_score()
        elif option == "2":
            print_subject_score()
        elif option == "3":
            print_students_rank()
        elif option == "4":
            print_name_data()
        elif option == "5":
            print("See you next time")
            exit_option = True
        else:
            print("Wrong input!! Please enter again.")
