import random  

def toss_coin():
    return random.choice(["Head", "Tail"])  

while True:
    user_input = input("Press Enter to flip the coin or type 'exit' to quit: ")  

    if user_input.lower() == "exit":
        print("Thanks for playing the game!")
        break

    coin_result = toss_coin()
    print(f"You got {coin_result}")  
    