# this is a Train1 project
# focus on input data and compile it

TXT_PATH = "/Users/ss580/Desktop/backand-wtf/練習1-3(2024.10.04)/grade.txt"  # 常數設置路徑


def load_txt(txt_path):
    data_full_list = []
    with open(txt_path, "r") as open_txt:  # 稱為不是寫入 注意開關檔 避免影響其他人存取檔案
        loaded_txt = open_txt.readlines()  # 先逐行讀出 讀完關掉在外面處理
    for data_line_str in loaded_txt:
        data_line_list = []
        for each_student in data_line_str.split():  # FIXME: variable name (row col line)
            if each_student.isdigit():  # 先判斷是不是數字是的話先轉換再寫入
                each_student = float(each_student)
            data_line_list.append(each_student)
        data_full_list.append(data_line_list)
    for each_person in data_full_list:  # 用全列表人數去跑迴圈
        each_person_total = 0
        for each_subject in each_person:  # 用每人科目去跑迴圈
            if isinstance(each_subject, float):
                each_person_total += each_subject  # 如果是數字就加入總分裡
        each_person_average = each_person_total / 3
        each_person.extend([each_person_total, each_person_average])
    return data_full_list  # 先只輸出數字方便後續練習使用


def print_txt(txt_unformatted_local):
    # FIXME:
    #  1. txt_unformatted_local.copy()
    #  2. line[index] = f-string: don't do that, use the commented method.
    data_full_list_unformatted = txt_unformatted_local
    data_full_list_str = []  # 用以儲存等等格式化後列表
    for line in data_full_list_unformatted:
        # line_list = []
        for index, each in enumerate(line):
            if isinstance(each, float):  # isdigit() 只能判斷"字串"中是否有數字
                line[index] = f"{each:.2f}"  # 在這邊將所有數字格式化到小數第二位
                # tmp = f-string
            # line_list.append(tmp)
        data_full_list_str.append(line)
    data_full_list_str.insert(0, ["name", "grade1", "grade2", "grade3", "total", "average"])
    for row in data_full_list_str:
        formated_row = [f"{item:>10}" for item in row]
        print(" ".join(formated_row))


if __name__ == "__main__":
    txt_unformatted = load_txt(TXT_PATH)
    print_txt(txt_unformatted)
    print(txt_unformatted[0][2], type(txt_unformatted[0][2]))
