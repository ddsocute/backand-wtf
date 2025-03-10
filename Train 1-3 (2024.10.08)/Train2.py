# this is a Train2 project
# focus on building five function to user

from Train1 import load_txt, print_txt, TXT_PATH

GRADE_FULL_LIST = load_txt(TXT_PATH)  # load data  write in main function
STUDENTS_LENGTH = len(GRADE_FULL_LIST)  # TODO: useless


def show_interface():
    print("""-------------------------------------------------
    1. Print students' grade
    2. Print subject scores
    3. Rank students
    4. Search for name
    5. Exit
    Please choose one and enter its number:\n""")


def print_student_score():
    txt_not_formated = load_txt(TXT_PATH)
    print_txt(txt_not_formated)


def print_subject_score():
    subject_size = len(GRADE_FULL_LIST[0][1:-2])  # 先隨邊挑一行確認總共有幾個grade
    # TODO:mmmm
    subject_list = [[] for _ in range(subject_size)]  # 依照成績數新增列表數量
    for each_student in GRADE_FULL_LIST:
        for index, subject in enumerate(each_student[1:-2]):  # 取第二到倒數第三的grade score
            subject_list[index].append(subject)  # 把每科成績輸入對應的列表中
            # TODO: calculate sum directly, append is not necessary.
    # subject_list = [[item for item in row[1:-2]] for row in GRADE_FULL_LIST]  # TODO
    for index, sum_list in enumerate(subject_list):  # 把每科列表數字起來得出每科總和
        print(f"grade{index + 1} total is: {sum(sum_list):.2f} ,"
              f" average is: {sum(sum_list) / len(GRADE_FULL_LIST):.2f}")   # TODO:計算跟顯示分開


def print_students_rank():
    each_student_average_list = []
    each_student_name_list = []
    for each_student_data_list in GRADE_FULL_LIST:
        each_student_average_list.append(each_student_data_list[-1])
        each_student_name_list.append(each_student_data_list[0])
    zipped = zip(each_student_name_list, each_student_average_list)  # 裝包
    sorted_zipped = sorted(zipped, key=lambda x: x[1], reverse=True)
    # zipped.sort()  # this line do not return anything.

    sorted_names, sorted_grades = zip(*sorted_zipped)  # 解包將zip回傳的迭代器裡的元組 重組成兩個元組 TODO
    for rank, name, grade in zip(range(1, len(GRADE_FULL_LIST) + 1), sorted_names, sorted_grades):
        # 用zip一一對應排名、名字與成績在輸出 TODO
        print(f"rank{rank} is {name:^7}  average grade is {grade:.2f}")  # 格式化輸出
    # for i in range(1, len(GRADE_FULL_LIST) + 1):
    #     rank, name, grade = i, sorted_names[i - 1], sorted_grades[i - 1]
    #     print()


def print_name_data():
    exit_print = False
    student_name_list = []
    head_line = ["name", "grade1", "grade2", "grade3", "total", "average"]
    find_name = input("please input the student name\n")
    for each_student in GRADE_FULL_LIST:
        student_name_list.append(each_student[0])  # 建立一個放學生名字的列表
    while not exit_print:
        # TODO: for-loop
        if find_name in student_name_list:
            find_list = GRADE_FULL_LIST[student_name_list.index(find_name)]  # 找到該學生所有資料
            for index, data in enumerate(find_list):
                if isinstance(data, float):  # 如果是數字先格式化到小數點第二位 後面才不會因為有名字而無法格式化
                    data = f"{data:>.2f}"
                print(f"{head_line[index]:^7} : {data:^7}")
            exit_print = True
        else:
            find_name = input(f"You enter the wrong name\n"
                              "please input the student name\n")


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
