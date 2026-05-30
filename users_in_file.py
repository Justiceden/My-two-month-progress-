
import json
seen=[]
information={}
def add_user(user,password):
    
    if user not in seen:
        valid=True
    else:
        print("Username taken")
        return
        
        
    digit=False
    special=False
    letter=False
    if len(password)>7:
        for ch in password:
            if ch.isdigit():
                digit=True
            elif ch.isalpha():
                letter=True
            else:
                special=True
        if special and digit and letter:
            print("User and password accpected")
            seen.append(user)
            information[user]=password
        else:
             print("Password must contain a letter,digit,and a special character")
             return
    else:
        print("Password must be bigger")
        return
        
    
    with open("/storage/emulated/0/userandpass.json","w") as file:
        
        json.dump(information,file)







    





















