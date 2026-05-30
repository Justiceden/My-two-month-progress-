import requests as rq,pandas as pd,numpy as np

response=rq.get("https://jsonplaceholder.typicode.com/users")

information=response.json()
information=pd.json_normalize(information)

df=pd.DataFrame(information)
unique=df[["name","email"]]



small_user=df[df["username"].apply(len)<7]

print(small_user[["username","name","email"]])


print(small_user.groupby("name")["email"].size())






















    





















