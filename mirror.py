import random

brain= random.choice(["west","east"])

while True:
    print("you hear a voice",brain)
    print("you awoken from a slumber \n two doors must pick one\n the left or the right one") 
    choice=input("left or right").lower()
    print("are you sure you want to open that door?")
    hard_choice=input("yes or no").lower()
    if brain== "west":
        if choice != "left":
            if hard_choice =="no":
                print("Go to sleep and come back")
                continue
            else:
                print("you open thr door...inside there is a mirror with your face in it")
                break
        else:
            if hard_choice=="no":
                print("Go to sleep and come back")
                continue
            else:
                if hard_choice =="yes":
                    print("Congratulations you escaped")
                    break
    else:
        if brain=="east":
            if choice == "left":
                if hard_choice =="no":
                    print("Go to sleep and come back")
                    continue
                else:
                    print("you open thr door...inside there is a mirror with your face in it")
                    break
            else:
                if hard_choice=="no":
                    print("Go to sleep and come back")
                    continue
                else:
                    if hard_choice =="yes":
                        print("Congratulations you escaped")
                        break
    
        
    





















