
# WORD SCRAMBLER

import random

print(" WORD SCRAMBLER ")

while True:
    word = input("\nEnter a word to start scrambling : ")
    if word.lower() == "quit":
        print("Goodbyeeee...")
        break

    letters = list(word)
    random.shuffle(letters)
    print(f"Scramble done : {"".join(letters)}")
