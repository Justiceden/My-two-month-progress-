import random as rn

health = 100
enemy_health = 100
berry = 3
state = "explore"

def enemy_turn():
    global health
    print("enemy turn")

    chance = rn.randint(1, 100)

    if chance <= 30:
        print("enemy missed")
    elif chance <= 90:
         health -= 20
        print("enemy hit you")
        if health <= 0:
            print("you died")
            return "dead"
    else:
        if chance <=100:
            health -= 40
        print("enemy hit you \n and its a critical hit")
        if health <= 0:
            print("you died")
            return "dead"

    return "continue"


def counter():
    global health, state

    chance = rn.randint(1, 100)

    if chance <= 30:
        print("you countered enemy attack \n enemy is dead")
        state = "explore"
        return "enemy_dead"

    else:
        print("you couldn't counter")
        health -= 30
        print("enemy hit you")

        if health <= 0:
            print("you died")
            return "dead"

    return "continue"


while True:

    if state == "explore":
        print("Your health:", health, "| Enemy health:", enemy_health)
        event = input("walk/heal: ").lower()

        if event == "heal":
            if berry == 0:
                print("No berry")
                continue

            berry -= 1
            health += 30

            if health > 100:
                health = 100

        elif event == "walk":
            chance = rn.randint(1, 100)

            if chance <= 30:
                print("You fell in trap")
                health -= 30

                if health <= 0:
                    print("you died")
                    break

            else:
                print("enemy found")
                enemy_health = 100
                state = "action"

    elif state == "action":
        print("Your health:", health, "| Enemy health:", enemy_health)
        choice = input("attack/counter/run: ").lower()

        if choice == "attack":
            chance = rn.randint(1, 100)

            if chance < 70:
                enemy_health -= 30
                print("hit")

                if enemy_health <= 0:
                    print("enemy dead")
                    state = "explore"
                    continue

                result = enemy_turn()

                if result == "dead":
                    break

            else:
                print("you missed")

                result = enemy_turn()

                if result == "dead":
                    break

        elif choice == "counter":
            result = counter()

            if result == "enemy_dead":
                continue

            elif result == "dead":
                break

            elif result == "continue":
                continue

        elif choice == "run":
            print("you escaped")
            state = "explore"
            continue

        else:
            print("invalid choice")























