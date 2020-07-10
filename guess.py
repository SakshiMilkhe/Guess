import random
#guess game

#get guess
def get_guess():
    return list(input("What is your guess\n"))

#generate the computer code
def generate_code():
    digits=[str(num) for num in range(10)]
    #shuffling the digits
    random.shuffle(digits)
    #then grab the first three after the shuffle
    return digits[:3]

#generate the clues
def generate_clues(code, user_guess):
    if(user_guess==code):
        return "CODE CRACKED!"
    clues=[]
    for ind, num in enumerate(user_guess):
        if(num==code[ind]):
            clues.append("MATCH")
        elif num in code:
            clues.append("CLOSE")
    if clues==[]:
        return["NOPE"]
    else:
        return clues

#run game logic
print("Welcome Code Breaker!")
secret_code=generate_code()
clue_report=[]
while clue_report!="CODE CRACKED!":
    guess=get_guess()
    clue_report=generate_clues(guess, secret_code)
    print("Here is the result of your guess: ")
    for clue in clue_report:
        print(clue)