#!/usr/bin/env python3

"""
Главный модуль игры 'Лабиринт Шиноби: Испытание Воли Огня'
Подключает базовые данные и определяет состояние игрока.
"""

#from labyrinth_game import player_actions, utils
from labyrinth_game.constants import ROOMS

# --- Состояние игры ---
game_state = {
    "player_inventory": [],  # Инвентарь игрока
    "current_room": "entrance",  # Текущая комната
    "game_over": False,  # Индикатор окончания игры
    "steps_taken": 0,  # Количество шагов, сделанных игроком
}


def show_current_room():
    """Выводит описание текущей комнаты."""
    current = game_state["current_room"]
    room = ROOMS[current]

    print(f"\n=== {current.upper()} ===")
    print(room["description"])
    print("\nВыходы:", ", ".join(room["exits"].keys()))
    if room["items"]:
        print("Предметы:", ", ".join(room["items"]))
    else:
        print("Предметов нет.")
    print("---------------------------")


# --- Временный запуск (для проверки базовой логики) ---
if __name__ == "__main__":
    print("Добро пожаловать в игру 'Лабиринт Шиноби: Испытание Воли Огня'!")
    show_current_room()

