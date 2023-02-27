import random


q = int(input("Enter the Turns you wnt to play:\n"))
s = 0
def game_w_l(you,comp):
    if comp==you:
        return None

    if comp=="r":
        if you=="p":
            return True
        elif you=="s":
            return False
    if comp=="p":
        if you=="s":
            return True
        elif you=="r":
            return False 
    if comp=="s":
        if you=="p":
            return False
        elif you=="r":
            return True
for i in range(q):
                
    print("comp turn Rock(r) paper(p) sesor(s): ")
    you = input("your turn Rock(r) paper(p) sesor(s): ")
    compt = random.randint(1,3)
    if compt == 1:
        comp = "r"
    elif compt == 2:
        comp = "p"
    elif compt ==3:
        comp = "s"
    print ("comp chose",comp)
    print ("you chose",you)
    a = game_w_l(you,comp)
    if a==None:
        print("game is ties")
    elif a:
        print("you win the game ")
        s = s+1
    else:
        print("you lose")
    
print(f"the score is {s}")

with open("high score.txt","r") as r:
    scorevalue = r.read()


with open("high score.txt","w") as f:
    f.write(str(s))

if s>int(scorevalue):
    print("********|you beat the high score|********")
else:
    print("#####<Game Over>#####")


