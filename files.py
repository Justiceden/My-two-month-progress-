def user_password():
    name=input()
    password=input()
    with open("/storage/emulated/0/account.txt","a") as file:
        file.write(name+":"+password+"\n")
        

user_password()























