# this is a Train1 project
# focus on input data and compile it

TXT_PATH = "/Users/ss580/Desktop/backand-wtf/練習1-3(2024.10.04)/grade.txt"


def show_txt():
    # data_line_str = "" 後面定義會覆蓋過 浪費
    # data_line_list = []
    data_full_list = []
    # each_person_total = 0
    with open(TXT_PATH, "r") as open_txt:  # 稱為不是寫入 注意開關檔 避免影響其他人存取檔案
        for data_line_str in open_txt:
            data_line_list = data_line_str.split()
            for i in range(1, 4):  # i for integer  可註解或設常數 最好是用型別判斷是否處禮(is digit)
                data_line_list[i] = float(data_line_list[i])
            data_full_list.append(data_line_list)
            # Jacky's code
            # result = []
            # for each in data_line_str.split():
            #     if each.isdigit():
            #         each = float(each)
            #     result.append(each)
            # end of Jacky's code
    data_full_list.insert(0, ["name", "grade1", "grade2", "grade3", "total", "average"])
    #一到後面
    for i in range(1, 7): #mmm
        each_person_total = 0
        for j in range(1, 4):#mmm
            each_person_total += data_full_list[i][j]# use sum() listslicing do some comment
        each_person_total_round = round(each_person_total, 2)
        data_full_list[i].append(each_person_total_round)
        each_person_avg_round = round(each_person_total / 3, 2)#mmm
        data_full_list[i].append(each_person_avg_round)
    return data_full_list


if __name__ == "__main__":
    print(*show_txt(), sep='\n')


