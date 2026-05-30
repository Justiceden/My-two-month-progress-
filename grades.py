import json

student_marks=student_marks = {
    "Arpit": 84.6,
    "friend1": 85,
    "friend2": 85,
    "friend3": 88,
    "friend4": 82.8,
    "friend5": 82.6,
    "friend6": 67.6,
    "friend7": 72.6,
    "friend8": 76,
    "friend9": 83.6
}
total=sum(student_marks.values())

length=len(student_marks)
average=total/length
student_marks["Average"]=average

with open("/storage/emulated/0/avg.json","w") as file:

    json.dump(student_marks,file,indent=4))







    





















