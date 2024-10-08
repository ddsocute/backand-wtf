# this is a Train2 project
# focus on building five function to user


from Train1 import load_txt, print_txt

TXT_PATH = "/Users/ss580/Desktop/backand-wtf/練習1-3(2024.10.04)/grade.txt"  # 常數設置路徑
GRADE_FULL_LIST = load_txt(TXT_PATH)
STUDENTS_LENGTH = len(GRADE_FULL_LIST)


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
    subject_list = [[] for _ in range(subject_size)]# 依照成績數新增列表數量
    for each_student in GRADE_FULL_LIST:
        for index, subject in enumerate(each_student[1:-2]):  # 取第二到倒數第三的grade score
            subject_list[index].append(subject)  # 把每科成績輸入對應的列表中
    for index, sum_list in enumerate(subject_list) :  # 把每科列表數字起來得出每科總和
        print(f"grade{index + 1} total is: {sum(sum_list):.2f} ,"
              f" average is: {sum(sum_list) / len(GRADE_FULL_LIST):.2f}")


def print_students_rank():
    eachperson_average_list = []
    eachperson_name_list = []
    for eachperson_data_list in GRADE_FULL_LIST:
        eachperson_average_list.append(eachperson_data_list[-1])
        eachperson_name_list.append(eachperson_data_list[0])
    zipped = zip(eachperson_name_list, eachperson_average_list)  # 裝包
    sorted_zipped = sorted(zipped, key=lambda x: x[1], reverse=True)
    sorted_names, sorted_grades = zip(*sorted_zipped)  # 解包將zip回傳的迭代器裡的元組 重組成兩個元組
    for rank, name, grade in zip(range(1, len(GRADE_FULL_LIST) + 1), sorted_names, sorted_grades):
        # 用zip一一對應排名、名字與成績在輸出
        print(f"rank{rank} is {name:^7s}  average grade is {grade:.2f}")  # 格式化輸出


def print_name_data():
    student_list = []
    head_line = ["name", "grade1", "grade2", "grade3", "total", "average"]
    find_name = input("please input the student name\n")
    for each_student in GRADE_FULL_LIST:
        student_list.append(each_student[0])  # 建立一個放學生名字的列表
    while True:
        if find_name in student_list:
            find_list = GRADE_FULL_LIST[student_list.index(find_name)]  # 找到該學生所有資料
            for index, data in enumerate(find_list):
                if isinstance(data, float):  # 如果是數字先格式化到小數點第二位 後面才不會因為有名字而無法格式化
                    data = f"{data:>.2f}"
                print(f"{head_line[index]:^7} : {data:^7}")
            break
        else:
            find_name = input(f"You enter the wrong name\n"
                              "please input the student name\n")


if __name__ == "__main__":
    while True:  # while bool (no ()):
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
            break
        else:
            print("Wrong input!! Please enter again.")
