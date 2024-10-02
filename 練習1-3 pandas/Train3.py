import pandas as pd


TXT_PATH = '/Users/ss580/Desktop/python/python/grade.txt'
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)


def interface():
    print("""-------------------------------------------------
    1. Print students' grade
    2. Print subject scores
    3. Rank students
    4. Search for name
    5. Find special student by word
    6. Exit
    Please choose one and enter its number:\n""")

# class student :
#     def __init__(self, name, grade1, grade2, grade3,total,average):
#         self.name = name
#         self.grade1 = grade1
#         self.grade2 = grade2ｔ
#         self.grade3 = grade3
#         self.total = grade1 + grade2 + grade3
#         self.average = self.total/3 ?????????????

class GradeManager:
    def __init__(self):
        self.grade = []
    def load(self,filename):
        self.df = pd.read_csv(filename, sep=" ", header=None, names=["name", "grade1", "grade2", "grade3"])
        self.df.set_index("name",inplace=True)
        self.df['grade1'] = self.df['grade1'].astype(float)
        self.df['grade2'] = self.df['grade2'].astype(float)
        self.df['grade3'] = self.df['grade3'].astype(float)
        self.df["total"] = self.df['grade1'] + self.df['grade2'] +self.df['grade3']
        self.df["average"] = (self.df['grade1'] + self.df['grade2'] +self.df['grade3'])/3
        self.df["total"] = self.df["total"].round(2)
        self.df["average"] = self.df["average"].round(2)
    def function1(self):
        print(self.df)
    def function2(self):
        subTot = self.df[["grade1","grade2","grade3"]].sum()
        avgTot = self.df[["grade1","grade2","grade3"]].sum()/3
        print("subject total is:\n",subTot)
        print("subject average is:\n",avgTot)
    def function3(self):
        self.df["rank"] = self.df["average"].rank(ascending = False)
        print(self.df)
    def function4(self):
        specialIndex = input("please enter the name\n")
        specialRow = self.df.loc[specialIndex]
        print(specialRow)
    def function5(self):
        specialIndex = self.df.index.str.contains(input("please enter the word\n"),case = False)
        specialRow = self.df.loc[specialIndex]
        print(specialRow)


gradeManager = GradeManager()
gradeManager.load(TXT_PATH)
conti = True
while(conti):
    interface()
    cho = input()
    if(cho == "1"):
        gradeManager.function1()
    elif(cho == "2"):
        gradeManager.function2()
    elif(cho == "3"):
        gradeManager.function3()
    elif(cho == "4"):
        gradeManager.function4()
    elif(cho == "5"):
        gradeManager.function5()
    elif(cho == "6"):
        print("See you next time")
        break

    else:
        print("Wrong input!! Please enter again.")


