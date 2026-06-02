import random
from utils import human_turn, computer_turn
from app_logic import check_winner, play_game
import time

def start_game():
    sticks=21
    turn=input("Хотите ходить первыми? (да/нет): ").strip().lower()
    if turn=="да":
        human_first=True
    else:
        human_first=False
    play_game(human_first,sticks)
    
start_game()
time.sleep(5)
