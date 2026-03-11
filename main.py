player_name=""
round_num=0
rounds=["Wellington Waterfront","Newtown"]

def welcome():
    global player_name
    global round_num
    print("Welcome to Language Racer!")
    print("")
    player_name=input("What is your name?")
    print("")
    print(f"Congratulations on starting your racing adventure {player_name}!")
    print("")
    round_num=1
    main_menu()
def main_menu():
    x=0
    print("Rounds:")
    print("")
    for i in rounds:
        print(rounds[x])
        x+=1
    print("")
    print(f"You are on Round {round_num}: {rounds[round_num-1]}")


welcome()

#main menu with season set out
#end goal is to win championship
#asked questions during race (language)
#car upgrades
#different tracks with different attributes
#rival tally
#different difficulty