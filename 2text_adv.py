# Text Adventure Script
# The Adventure game uses just the Time module to begin 
# with, creating pauses between print functions. 
# There's a help system in place to expand upon, as well as the story itself.

import time
print("\n" * 200)
print("<<<<<Awesome Adventure>>>>")
print("\n" * 3)
time.sleep(3)
print("\n A long time ago, a warrior strode forth from the frozen north.")
time.sleep(1)
print("Does this warrior have a name?")
name=input("> ")
print(name, "the barbarian, sword in hand and looking for adventure!")
time.sleep(1)
print("However, evil is lurking nearby....")
time.sleep(1)
print("A pair of bulbous eyes regards the hero...")
time.sleep(1)
print("Will", name, "prevail, and win great fortune...")
time.sleep(1)
print("Or die by the hands of great evil...?")
time.sleep(1)
print("\n" *3)
print("Only time will tell...")
time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(5)

print(''' You find yourself at a small inn. There's 
little gold in your purse but your sword is sharp, 
and you're ready for adventure.
With you are three other customers.
A ragged looking man, and a pair of dangerous 
looking guards.''')

def main():
    print("\n ----------")
    print("Do you approach the...")
    print("\n")
    print("1. Ragged looking man")
    print("2. Dangerous looking guards")
    print("help - in case you wonder")
    cmdlist = ["1", "2"]
    
    def getcmd(cmdlist):
        cmd = input(name+">")
        if cmd in cmdlist:
            return cmd
        elif cmd == "help":
            print("Enter your choices as detailed in the game.")
            print("or enter ‘quit’ to leave the game")
            return getcmd(cmdlist)
        elif cmd == "quit":
            print("\n-----------")
            time.sleep(1)
            print("Sadly you return to your homeland without \nfame or fortune...")
            time.sleep(5)
            exit()
    
    cmd = getcmd(cmdlist)
    if cmd == "1":
        def ragged():
            print("\n" * 200)
            print('''You walk up to the ragged looking man and 
            greet him.
            He smiles a toothless grin and, with a strange 
            accent, says.
            "Buy me a cup of wine, and I’ll tell you of 
            great treasure...''')
            time.sleep(2)
        ragged()
    elif cmd == "2":
        def guards():
            print("\n" *200)
            print('''You walk up to the dangerous looking guards 
            and greet them.
            The guards look up from their drinks and 
            snarl at you.
            "What do you want, barbarian?" One guard reaches 
            for the hilt of his sword...''')
            time.sleep(2)
        guards()
       
if __name__ == "__main__" :
    main()