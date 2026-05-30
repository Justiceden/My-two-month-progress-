import pandas as pd
student_marks={"Name":["Arpit","Sam","Sameul"],
"Age":[11,12,13]}
    
def space():
    print("\n"*4)

list=pd.DataFrame(student_marks,index=["Student 1","Student 2","Student 3"])



jack=pd.DataFrame([{"Name":"Jack","Age":14}],index=["Student 4"])

list=pd.concat([list,jack])
print(list)


space()

list["Marks"]=[11,12,13,42]
print(list)

space()

print(list.loc["Student 4"])

space()

print(list.iloc[3])


list.loc["Student 4","Name"]="Araragi"

space()

print(list)















    





















