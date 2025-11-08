# labyrinth_game/utils.py
from labyrinth_game.constants import ROOMS
from labyrinth_game import player_actions, constants
import math

def describe_current_room(game_state):
    current = game_state["current_room"]
    room = ROOMS[current]

    print(f"\n=== {current.upper()} ===")
    print(room["description"])

    if room["items"]:
        print("Заметные предметы:", ", ".join(room["items"]))
    else:
        print("Предметов нет.")

    print("Выходы:", ", ".join(room["exits"].keys()))

    if room["puzzle"] is not None:
        print("Кажется, здесь есть загадка (используйте команду solve).")
    print("---------------------------")

def pseudo_random(seed, modulo):
    x = math.sin(seed * 12.9898) * 43758.5453
    frac = x - math.floor(x)
    return int(frac * modulo)

def trigger_trap(game_state):
    print("Ловушка активирована! Пол стал дрожать...")
    inventory = game_state["player_inventory"]
    if inventory:
        idx = pseudo_random(game_state["steps_taken"], len(inventory))
        lost_item = inventory.pop(idx)
        print(f"Вы потеряли предмет: {lost_item}")
    else:
        chance = pseudo_random(game_state["steps_taken"], 10)
        if chance < 3:
            print("Вы получили смертельный урон! Игра окончена.")
            game_state["game_over"] = True
        else:
            print("Вы чудом уцелели!")

def random_event(game_state):
    if pseudo_random(game_state["steps_taken"], 10) != 0:
        return
    event_type = pseudo_random(game_state["steps_taken"] + 1, 3)
    current_room = ROOMS[game_state["current_room"]]
    inventory = game_state["player_inventory"]
    if event_type == 0:
        print("На полу вы замечаете блестящую монетку!")
        current_room["items"].append("coin")
    elif event_type == 1:
        print("Вы слышите шорох вдалеке...")
        if "sword" in inventory:
            print("Благодаря вашему мечу, существо испугалось и убежало.")
    elif event_type == 2:
        if game_state["current_room"] == "trap_room" and "torch" not in inventory:
            print("Опасность! Вы видите ловушку впереди!")
            trigger_trap(game_state)

def solve_puzzle(game_state):
    current = game_state["current_room"]
    room = ROOMS[current]

    if not room["puzzle"]:
        print("Загадок здесь нет.")
        return

    question, answer = room["puzzle"]
    print(question)
    user_answer = player_actions.get_input("Ваш ответ: ").strip().lower()

    alt_answers = {
        "10": ["10", "десять"],
        "шаг шаг шаг": ["шаг шаг шаг"],
        "резонанс": ["резонанс"]
    }

    valid_answers = alt_answers.get(answer.lower(), [answer.lower()])

    if user_answer in valid_answers:
        print("Правильно! Вы решили загадку.")
        room["puzzle"] = None
        if current == "trap_room" and "rusty_key" not in game_state["player_inventory"]:
            game_state["player_inventory"].append("rusty_key")
            print("Вы получили rusty_key!")
        elif current != "trap_room" and "treasure_key" not in game_state["player_inventory"]:
            game_state["player_inventory"].append("treasure_key")
            print("Вы получили treasure_key!")
    else:
        print("Неверно. Попробуйте снова.")
        if current == "trap_room":
            trigger_trap(game_state)

def attempt_open_treasure(game_state):
    current = game_state["current_room"]
    room = ROOMS[current]

    if "treasure_chest" not in room["items"]:
        print("Сундук уже открыт.")
        return

    if "treasure_key" in game_state["player_inventory"]:
        print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
        room["items"].remove("treasure_chest")
        print("В сундуке сокровище! Вы победили!")
        game_state["game_over"] = True
        return

    answer = player_actions.get_input("Сундук заперт. Хотите попробовать ввести код? (да/нет) ").strip().lower()
    if answer == "да":
        code = player_actions.get_input("Введите код: ").strip()
        if room["puzzle"] and code in ["10", "десять"]:
            print("Код верный! Сундук открыт!")
            room["items"].remove("treasure_chest")
            print("В сундуке сокровище! Вы победили!")
            game_state["game_over"] = True
        else:
            print("Неверный код.")
    else:
        print("Вы отступаете от сундука.")

def show_help(COMMANDS):
    print("\nДоступные команды:")
    for cmd, desc in COMMANDS.items():
        print(f"{cmd:<16} - {desc}")
