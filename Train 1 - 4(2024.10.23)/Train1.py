# this is a Train1 project
# focus on input data and compile it

# '/Users/ss580/Desktop/backand-wtf/Train 1 - 4(2024.10.23)/Grades.txt'
TXT_PATH = ("/Users/ss580/Desktop/backand-wtf/"
            "Train 1 - 4(2024.10.23)/Grades.txt")


# 常數設置路徑


def load_txt(txt_path):
    """
    load file to list
    :param txt_path: file path
    :return: List contain students' name and grades
    """
    full_list_unformatted = []
    line_list = []
    with open(TXT_PATH, "r") as open_txt:
        # 稱為不是寫入 注意開關檔 避免影響其他人存取檔案
        loaded_txt = open_txt.readlines()
        # 先逐行讀出 讀完關掉在外面處理

    for index, row in enumerate(loaded_txt):
        temperate_list = []
        total = 0
        subject_size = 0
        for column in row.split():
            if column.isdigit() and int(column) <= 100:
                # 先判斷是不是數字是的話先轉換再寫入
                column = float(column)
                total += column
                subject_size += 1
            temperate_list.append(column)
        average = total / subject_size
        line_list.extend(temperate_list + [total, average])
        if len(temperate_list) < len(loaded_txt[0].split()):
            full_list_unformatted[-1].extend(line_list.copy())
            line_list.clear()
            continue
        else:
            full_list_unformatted.append(line_list.copy())
            line_list.clear()
    unformatted_list = full_list_unformatted.copy()
    # unformatted_list.insert(0, ["name", "phone", "grade1", "grade2", "grade3",
    #                             "total", "average"])
    full_list_str = []

    # 用以儲存格式化後的列表
    for row in unformatted_list:
        for index, column in enumerate(row):
            if isinstance(column, float):  # 如果是浮點數，格式化為 10 寬度並保留 2 位小數
                row[index] = f"{column:^15.2f}"
            else:  # 其他情況直接居中格式化為 10 寬度
                row[index] = f"{str(column):^15}"
        full_list_str.append(row)
    return full_list_str


def print_txt(full_list_unformatted):
    """
    format grades list returned from load_txt and print it
    :param unformatted_list: unformatted grades list returned from load_txt
    :return: grades list have been formatted
    """
    # FIXME:
    #  1. txt_unformatted_local.copy()
    #  2. line[index] = f-string: don't do that, use the commented method.
    unformatted_list = full_list_unformatted.copy()
    unformatted_list.insert(0, ["name", "phone", "grade1", "grade2", "grade3",
                                "total", "average"])
    full_list_str = []

    # 用以儲存格式化後的列表
    for row in unformatted_list:
        for index, column in enumerate(row):
            if isinstance(column, float):  # 如果是浮點數，格式化為 10 寬度並保留 2 位小數
                row[index] = f"{column:^15.2f}"
            else:  # 其他情況直接居中格式化為 10 寬度
                row[index] = f"{str(column):^15}"
        full_list_str.append(row)
    return full_list_str
    # print(*full_list_str, sep='\n')


if __name__ == "__main__":
    print(*load_txt(TXT_PATH), sep="\n")
