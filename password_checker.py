
#Remove spaces at start/end
#Ignore empty usernames
#Username must be at least 5 characters
#Must contain at least 1 letter AND 1 number
#Convert everything to lowercase
password=input().strip()
is_digit=False
is_letter=False

if len(password) >=8 :
    for letter in password :
        if letter.isdigit():
            is_digit=True
        if letter.isalpha():
            is_letter =True
    if is_digit and is_letter :
        print("Valid password")
    else:
        if is_digit==False:
            print("must have number")
        if is_letter == False:
            print("must have letter")
else:
    print("Password must be longer")    





    





















