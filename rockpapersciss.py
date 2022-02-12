import random

def play():
    user = input('r for rock, p for paper, s for scissors')
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'tie'

    if is_win(user,computer):
        return 'You Won!'

    return 'You Lose!'

def is_win(player,opponent):
    #returns true if player wins
    if (player == 'p' and opponent == 'r') or (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p'):
        return True
    return False

print(play())