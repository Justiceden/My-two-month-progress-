import random
health = 100  
food = 0
bag = food
random_event = None
food += 1
scroll = 1
while True:
    

    print("what do you wish to do? \n walk or meditate")
    choice = input("walk,meditate").lower()

    if choice != "walk":
        scroll -= 1
        print(scroll)
        if scroll == 0:
            print("you must walk first")
        else:
            health += 20
            if health > 100:
                health = 100
            print(health)

    elif choice == "walk":
        probability = random.randint(1, 100)

        #if probability < 50:
       #     random_event = "food"
        if probability < 80:
            random_event = "enemy"
        else:
            random_event = "trap"
            health -= 10
            print(health)

        if health < 1:
            print("you died")
            break

        if random_event == "enemy":
            print("enemy attack\n what do you wish to do?")
            options = input("attack,run ").lower()

            if options == "attack":
                event = random.randint(1, 100)
                if event > 80:
                    scroll += 1
                    print("you killed the mob and got something\n +1 scroll")
                else:
                    health -= 20
                    print("you are hit")
                    if health < 1:
                        print("you died")
                        break
                continue 

            elif options == "run":
                print("you got away")
                continue

















