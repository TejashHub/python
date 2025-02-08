import random
import itertools

deck = list(itertools.product(range(1, 14), ["Spade", "Club", "Hearts", "Diamond"]))

random.shuffle(deck)

for i in range(5):
    print(f'{(deck[i][0], "of", deck[i][1])}')

