# this is a xxx project
# focus on XXX functions and XXX

import pandas as pd

# read and download
grade = pd.read_csv(
    "/練習1-3(2024.10.04)/grade.txt",
    sep=" ",
    header=None,
    names=["name", "grade1", "grade2", "grade3"],
)
grade.set_index("name", inplace=True)
grade['grade1'] = grade['grade1'].astype(float)
grade['grade2'] = grade['grade2'].astype(float)
grade['grade3'] = grade['grade3'].astype(float)
grade["total"] = grade['grade1'] + grade['grade2'] + grade['grade3']
grade["average"] = (grade['grade1'] + grade['grade2'] + grade['grade3']) / 3
grade["total"] = grade["total"].round(2)
grade["average"] = grade["average"].round(2)
print(grade)
