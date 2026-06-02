from utils import human_turn, computer_turn

def check_winner(sticks_left):
    if sticks_left==0:
        return True
    return False

def play_game(human_first,sticks):
    current_player=human_first
    while sticks>0:
        if current_player:
            taken=human_turn(sticks)
        else:
            taken=computer_turn(sticks)
        sticks-=taken
        current_player=not current_player
        if check_winner(sticks):
            winner="Вы победили!" if current_player else "Победил компьютер"
            print(winner)
            break
