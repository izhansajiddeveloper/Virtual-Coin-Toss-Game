
def toss_coin():
    return random.choice("head","Tail")

while True:
    user_input = ("press enter to flip the coin or type exit to quit")
    if(user_input.lower()=="exit"):
        print("Thanks for playing the game")
        break
    coin_result=toss_coin()
    print(f"You rolled a {toss_coin})")