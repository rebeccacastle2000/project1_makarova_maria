#!/usr/bin/env python3
from labyrinth_game.constants import ROOMS
from labyrinth_game import utils, player_actions

def process_command(game_state, command):
    parts = command.strip().lower().split(maxsplit=1)
    cmd = parts[0]
    arg = parts[1] if len(parts) > 1 else None

    if cmd in ["north", "south", "east", "west"]:
        player_actions.move_player(game_state, cmd)
        return

    match cmd:
        case "look" | "осмотреться":
            utils.describe_current_room(game_state)
        case "inventory":
            player_actions.show_inventory(game_state)
        case "go":
            if arg:
                player_actions.move_player(game_state, arg)
            else:
                print("Укажите направление.")
        case "take":
            if arg:
                player_actions.take_item(game_state, arg)
            else:
                print("Укажите предмет для взятия.")
        case "use":
            if arg:
                player_actions.use_item(game_state, arg)
            else:
                print("Укажите предмет для использования.")
        case "solve":
            current_room = game_state["current_room"]
            if "treasure_chest" in ROOMS[current_room]["items"]:
                utils.attempt_open_treasure(game_state)
            else:
                utils.solve_puzzle(game_state)
        case "help":
            utils.show_help()
        case "quit" | "exit":
            print("Выход из игры.")
            game_state["game_over"] = True
        case _:
            print("Неизвестная команда.")

def main():
    game_state = {
        "player_inventory": [],
        "current_room": "entrance",
        "game_over": False,
        "steps_taken": 0,
    }

    print("Добро пожаловать в игру 'Лабиринт: Поиск сокровищ'!")
    utils.describe_current_room(game_state)

    while not game_state["game_over"]:
        command = player_actions.get_input("> ")
        process_command(game_state, command)

if __name__ == "__main__":
    main()


