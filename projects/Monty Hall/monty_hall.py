import random

images = ["🚪", "🐐", "🏆"]
doors_images = ["🚪", "🚪", "🚪"]


# create 3 doors
def shuffle_doors():
    door_list = ["goat", "goat", "prize"]
    random.shuffle(door_list)
    print(door_list)
    return door_list


# user pick door
def pick_door(doors):
    while True:
        pick = input("Which door you pick? ")
        if pick.isdigit():
            pick = int(pick)
            if 0 < pick < 4:
                if doors.index("prize") == pick - 1:
                    goat_door = random.choice([i for i in range(0, 3) if i != pick - 1])
                else:
                    goat_door = random.choice([i for i in range(0, 3) if i not in [pick - 1, doors.index("prize")]])
                doors_images[goat_door] = images[1]
                print("Revealing one door.")
                print(doors_images)
                break
            else:
                print("Enter door number 1 - 3. ")
        else:
            print("It's not a number. ")
    return pick - 1, goat_door


def change_door(user_pick):
    pick_change = input("Do you want to change doors? Y/N ")
    if pick_change.upper() == "Y":
        while True:
            pick = input("Which door you pick? ")
            if pick.isdigit():
                pick = int(pick)
                if 0 < pick < 4:
                    break
                else:
                    print("Enter door number. ")
            else:
                print("It's not a number. ")
        return pick - 1
    else:
        user_pick = user_pick
        return user_pick


def game_over(doors, user_pick):
    if doors[user_pick] == "prize":
        print("You win a prize!")
    else:
        print("You lost, you get a goat.")
    doors_images[doors.index("prize")] = images[2]
    print(doors_images)


def play_again():
    play = input("Do you want to play again? Y/N ")
    if play.upper() == "Y":
        print("\n")
        return True
    else:
        return False


def game():
    doors = shuffle_doors()
    user_pick, goat_door_1 = pick_door(doors=doors)
    change = change_door(user_pick=user_pick)
    if change != user_pick:
        user_pick = change
    game_over(doors=doors, user_pick=user_pick)


win = 0
games_played = 0
play = True
while play:
    print("Pick a door.")
    print("1.🚪 | 2.🚪 | 3.🚪")

    game()
    if play_again():
        games_played += 1
        print(games_played)
        if games_played > 0 and win > 1:
            print(f"Wins: {win}, winrate: {(games_played / win) * 100}%")
        doors_images = ["🚪", "🚪", "🚪"]
        play = True
    else:
        play = False
