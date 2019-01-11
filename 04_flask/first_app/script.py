import random

def pick_lotto():
    numbers = random.sample(range(1, 45 +1), 6)
    return numbers

print(pick_lotto())
