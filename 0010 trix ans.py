hand = [1, 0, 0]

def aTrick(h1: list):
    h2 = h1.copy()
    h2[0] = h1[1]
    h2[1] = h1[0]
    return h2

def bTrick(h1: list):
    h2 = h1.copy()
    h2[1] = h1[2]
    h2[2] = h1[1]
    return h2

def cTrick(h1: list):
    h2 = h1.copy()
    h2[0] = h1[2]
    h2[2] = h1[0]
    return h2

swap = str(input("please enter abc...: ", ))
swap = swap.lower()

for i in range(len(swap)):
    if swap[i] is "a":
        hand = aTrick(hand)
    elif swap[i] is "b":
        hand = bTrick(hand)
    elif swap[i] is "c":
        hand = cTrick(hand)

for i in range(3):
    if hand[i] == 1:
        ball = i+1

print(ball)