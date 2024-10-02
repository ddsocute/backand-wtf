import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

conti = True

# read and download
grade = pd.read_csv('/Users/ss580/Desktop/python/python/grade.txt', sep=" ", header=None,
                    names=["name", "grade1", "grade2", "grade3"])
grade.set_index("name", inplace=True)
grade['grade1'] = grade['grade1'].astype(float)
grade['grade2'] = grade['grade2'].astype(float)
grade['grade3'] = grade['grade3'].astype(float)
grade["total"] = grade['grade1'] + grade['grade2'] + grade['grade3']
grade["average"] = (grade['grade1'] + grade['grade2'] + grade['grade3']) / 3
grade["total"] = grade["total"].round(2)
grade["average"] = grade["average"].round(2)


def function1():
    print(grade)


def function2():
    sub_tot = grade[["grade1", "grade2", "grade3"]].sum()
    avg_tot = grade[["grade1", "grade2", "grade3"]].sum() / 3
    print("subject total is:\n", sub_tot)
    print("subject average is:\n", avg_tot)


def function3():
    grade["rank"] = grade["average"].rank(ascending=False)
    print(grade)


def function4():
    special_index = input("please enter the name\n")
    specialRow = grade.loc[special_index]
    print(specialRow)


def function6():
    specialIndex = grade.index.str.contains(input("please enter the word\n"), case=False)
    special_row = grade.loc[specialIndex]
    print(special_row)


def interface():
    print("""-------------------------------------------------
    1. Print students' grade
    2. Print subject scores
    3. Rank students
    4. Search for name
    5. Exit
    6. Find special student by word
    Please choose one and enter its number:\n""")


# if __name__ == '__main__':

conti = True  # continue, continue_state
while (conti):  # while bool (no ()):
    interface()
    cho = input()
    if (cho == "1"):
        function1()
    elif (cho == "2"):
        function2()
    elif (cho == "3"):
        function3()
    elif (cho == "4"):
        function4()
    elif (cho == "5"):
        print("See you next time")
        break
    elif (cho == "6"):
        function6()
    else:
        print("Wrong input!! Please enter again.")
