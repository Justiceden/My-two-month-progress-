import pandas as pd

data = {
    "Name": ["Arpit", "Sam", "Samuel", "Jack"],
    "Age": [11, 12, 13, 14],
    "Marks": [78, 85, 91, 67]
}

students = pd.DataFrame(data,
index=["Student 1", "Student 2", "Student 3", "Student 4"])



def space():
    print("\n"*4)
#Print the whole DataFrame.
#Print only the "Name" column.
#Print the row "Student 3" using loc.
#Print the second row using iloc.
#Change Jack’s marks from 67 to 95.
#Add a new column called "Passed":
#True if marks are above 70
#False otherwise
#Print students whose marks are greater than 80.
#Print only "Name" and "Marks" columns.
#Add a new student:

print(students.to_string())

space()

print(students["Name"].to_string())

space()

print(students.loc["Student 3"])

space()

print(students.iloc[1])

space()

students.loc["Student 4","Marks"]=95

space()

students["Passed"]=students["Marks"]>80
print(students)

space()


print(students[students["Marks"]>80])

space()

print(students[["Name","Marks"]])

space()


Aana=pd.DataFrame([{"Name":"Aana","Age":17,"Marks":90}],index=["Student 5"])


students=pd.concat([students ,Aana])

print(students)





















    





















