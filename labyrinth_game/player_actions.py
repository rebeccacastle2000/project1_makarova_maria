# labyrinth_game/player_actions.py
from labyrinth_game.constants import ROOMS
from labyrinth_game import utils

def show_inventory(game_state):
    inventory = game_state["player_inventory"]
    if inventory:
        print("В вашем инвентаре:", ", ".join(inventory))
    else:
        print("Инвентарь пуст.")

def get_input(prompt="> "):
    try:
        return input(prompt).strip()
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"

def move_player(game_state, direction):
    current_room = game_state["current_room"]
    room_data = ROOMS[current_room]
    exits = room_data["exits"]

    if direction in exits:
        next_room = exits[direction]
        # проверка на treasure_room и rusty_key
        if next_room == "treasure_room" and "rusty_key" not in game_state["player_inventory"]:
            print("Дверь заперта. Нужен ключ, чтобы пройти дальше.")
            return
        elif next_room == "treasure_room":
            print("Вы используете найденный ключ, чтобы открыть путь в комнату сокровищ.")
        game_state["current_room"] = next_room
        game_state["steps_taken"] += 1
        utils.describe_current_room(game_state)
        utils.random_event(game_state)
    else:
        print("Нельзя пойти в этом направлении.")

def take_item(game_state, item_name):
    room = ROOMS[game_state["current_room"]]

    if item_name == "treasure_chest":
        print("Вы не можете поднять сундук, он слишком тяжелый.")
        return

    if item_name in room["items"]:
        game_state["player_inventory"].append(item_name)
        room["items"].remove(item_name)
        print(f"Вы подняли: {item_name}")
    else:
        print("Такого предмета здесь нет.")

def use_item(game_state, item_name):
    if item_name not in game_state["player_inventory"]:
        print("У вас нет такого предмета.")
        return

    if item_name == "torch":
        print("Вы зажгли факел, стало светлее.")
    elif item_name == "sword":
        print("Вы чувствуете уверенность и готовность к любым испытаниям.")
    elif item_name == "bronze_box":
        print("Вы открыли бронзовую шкатулку.")
        if "rusty_key" not in game_state["player_inventory"]:
            game_state["player_inventory"].append("rusty_key")
            print("Вы нашли rusty_key!")
    else:
        print("Вы не знаете, как использовать этот предмет.")
