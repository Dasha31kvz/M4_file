import random
from utils import human_turn, computer_turn
from app_logic import check_winner
import time

def start_game():
    sticks=21
    turn=input("Хотите ходить первыми? (да/нет): ").strip().lower()
    if turn=="да":
        humam_first=True
    else:
        human_first=False
    play_game(human_first,sticks)

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
start_game()
time.sleep(5)
