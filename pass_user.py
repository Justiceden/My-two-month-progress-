

all_username=[]

def user_check():
    
    user=input("Enter desired username")
    if len(user)<=3:
        print("Username too short \n must be longer than 3 letters")
    elif len(user)>50:
        print("Username too long \n must be shorter than 51 characters")
    elif user in all_username:
        print("Username taken")
    else:
        all_username.append(user)
        print("Username accpected")
        return user
        
        
def password_check():
    letter_present=False
    number_present=False
    special_character=False
    password=input("Enter desired password:")
    if len(password) <8:
        print("Password must be atleast 8 characters long")
        return None
    for letter in password:
        if letter.isalpha():
            letter_present=True
        
        elif letter.isdigit():
            number_present=True
        else:
            special_character=True
    if letter_present==False:
        print("Password must contain a letter")
    elif number_present==False:
        print("Password must contain a number")
    elif special_character==False:
        print("Password must contain a special character" )
    else:
        print("Password accpected")
        return password 
        
        
        
        
        
user=user_check()
password =password_check()               
if user and password:
    with open("/storage/emulated/0/app.txt","a") as file:
       
        file.write(user+":"+password+"\n")



    





















