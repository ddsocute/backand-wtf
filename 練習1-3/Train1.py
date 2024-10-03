# this is a Train1 project
# focus on input data and compile it

TXT_PATH = "/Users/ss580/Desktop/backand-wtf/練習1-3/grade.txt"

def show_txt():
    data_line_str = ""
    data_line_list = []
    data_full_list = []
    each_person_list = []
    each_person_total = 0
    with open(TXT_PATH, "r") as open_txt:
        for data_line_str in open_txt:
            data_line_list = data_line_str.split()
            for i in range(1, 4):
                data_line_list[i] = float(data_line_list[i])
            data_full_list.append(data_line_list)
        data_full_list.insert(0, ["name", "grade1", "grade2", "grade3", "total", "average"])
        for i in range(1, 7):
            each_person_total = 0
            for j in range(1, 4):
                each_person_total += data_full_list[i][j]
            each_person_total_round = round(each_person_total, 2)
            data_full_list[i].append(each_person_total_round)
            each_person_avg_round = round(each_person_total / 3, 2)
            data_full_list[i].append(each_person_avg_round)
        print(*data_full_list, sep='\n')


if __name__ == "__main__":
    show_txt()


