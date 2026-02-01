from labyrinth_game.constants import ROOMS
from labyrinth_game.utils import describe_current_room, random_event


def show_inventory(game_state):
    if not game_state["player_inventory"]:
        print("\nВаш инвентарь пуст.")
    else:
        print("\nВаш инвентарь:")
        for item in game_state["player_inventory"]:
            print(f"  - {item}")


def get_input(prompt="> "):
    try:
        return input(prompt).strip()
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"


def move_player(game_state, direction):
    current_room = game_state["current_room"]
    room = ROOMS[current_room]

    if direction not in room["exits"]:
        print("Нельзя пойти в этом направлении.")
        return

    next_room = room["exits"][direction]

    if next_room == "treasure_room":
        if "rusty_key" in game_state["player_inventory"]:
            print("Вы используете найденный ключ, чтобы открыть путь")
            print("в комнату сокровищ.")
            game_state["current_room"] = next_room
            game_state["steps_taken"] += 1
            print(f"\nВы пошли на {direction}.")
            describe_current_room(game_state)
            random_event(game_state)
        else:
            print("Дверь заперта. Нужен ключ, чтобы пройти дальше.")
        return

    game_state["current_room"] = next_room
    game_state["steps_taken"] += 1
    print(f"\nВы пошли на {direction}.")
    describe_current_room(game_state)
    random_event(game_state)


def take_item(game_state, item_name):
    current_room = game_state["current_room"]
    room = ROOMS[current_room]

    if item_name == "treasure_chest":
        print("Вы не можете поднять сундук, он слишком тяжелый.")
        return

    if item_name in room["items"]:
        room["items"].remove(item_name)
        game_state["player_inventory"].append(item_name)
        print(f"Вы подняли: {item_name}")
    else:
        print("Такого предмета здесь нет.")


def use_item(game_state, item_name):
    if item_name not in game_state["player_inventory"]:
        print("У вас нет такого предмета.")
        return

    if item_name == "torch":
        print("Вы зажгли факел. Стало светлее, и вы лучше видите окружение.")
    elif item_name == "sword":
        print("Вы взяли меч в руки. Чувствуете себя увереннее.")
    elif item_name == "bronze_box":
        if "rusty_key" not in game_state["player_inventory"]:
            game_state["player_inventory"].append("rusty_key")
            print("Вы открыли бронзовую шкатулку. Внутри лежит ржавый ключ!")
        else:
            print("Шкатулка уже пуста.")
    elif item_name == "ancient_book":
        print("Вы пролистали древнюю книгу. На полях заметки о загадках")
        print("лабиринта.")
    elif item_name == "rusty_key":
        print("Этот ключ выглядит хрупким. Возможно, он подойдёт к какой-то")
        print("двери.")
    else:
        print(f"Вы не знаете, как использовать {item_name}.")