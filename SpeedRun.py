import time
import random

class AST():
    def __init__(self):
        self.held = None
        self.royal = None
        self.in_hand = None
        
    def __str__(self):
        return "Current status\n" + "Held: " + str(self.held) + "\n" + "Royal: " + str(self.royal) + "\n"
        
cards = ['Balance', 'Ewer', 'Spire', 'Spear', 'Arrow', 'Bole']
held = None
royal = None

def detect_balance(card):
    if card == 0:
        if ast.held is None:
            ast.held = True
            print('You gain the effect Balance held')
            return 1
    return 0
    
def detect_aoe(card):
    if card == 1 or card == 2:
        if ast.royal is None:
            ast.royal = True
            print('You gain the effect of Expanded Royal Road')
            return 1
    return 0
    
def start_pull():
    print("Pulling in 25 seconds! <se.10>")
    i = random.randint(0,5)
    if i == 4:
        print("Whoops the warrior forgot to hit vengence and lost his stacks")
        wait = 120
        return wait
    time.sleep(5)
    i = random.randint(0,5)
    if i == 4:
        print("The ninja messed up his Mudara")
        wait = 120
        return wait
    print("Pulling in 20 seconds. <se.10>")
    time.sleep(5)
    print("Pulling in 15 seconds. <se.10>")
    time.sleep(5)
    print("Pulling in 10 seconds. <se.10>")
    i = random.randint(0,5)
    if i == 4:
        print("Wait don't pull I think im lagging")
        wait = 120
        return wait
    time.sleep(3)
    print("Pulling in 7 seconds. <se.10>")
    time.sleep(1)
    print(6)
    time.sleep(1)
    print("5 <se.5>")
    time.sleep(1)
    print("4 <se.5>")
    time.sleep(1)
    print("3 <se.5>")
    time.sleep(1)
    print("2 <se.5>")
    time.sleep(1)
    print("1 <se.5>")
    time.sleep(1)
    i = random.randint(0,5)
    if i == 4:
        print("Someone pulled early XD")
        wait = 120
        return wait
    print("Pulling!")
    time.sleep(20)
    print("I messed up my opener we may as well just wipe.")
    print("I'm clipping anyway.")
    print("Of course I waste all my crits on the trash pull.")
    wait = 120
    return wait
    
ast = AST()
while True:
    wait = 30
    i = random.randint(0,5)
    print("You drew a " + cards[i])
    if i >= 3:
        i = random.randint(0,5)
        print("You throw away the card and draw a " + cards[i])
    b = detect_balance(i)
    a = detect_aoe(i)
    if b == 0 and a == 0 and i == 0:
        wait = start_pull()
        ast.royal = None
        ast.held = None
        
    print("Waiting on cooldowns to draw again. " + str(wait) + " seconds")
    print(ast)
    time.sleep(wait)
        