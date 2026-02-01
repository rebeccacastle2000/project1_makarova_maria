import math

from labyrinth_game.constants import COMMANDS, ROOMS


def pseudo_random(seed, modulo):
    value = math.sin(seed * 12.9898) * 43758.5453
    fractional = value - math.floor(value)
    result = fractional * modulo
    return int(math.floor(result))


def trigger_trap(game_state):
    print("\nЛовушка активирована! Пол стал дрожать...")

    if game_state["player_inventory"]:
        inv_len = len(game_state["player_inventory"])
        idx = pseudo_random(game_state["steps_taken"], inv_len)
        lost_item = game_state["player_inventory"].pop(idx)
        print(f"Вы потеряли предмет: {lost_item}")
    else:
        damage_roll = pseudo_random(game_state["steps_taken"], 10)
        if damage_roll < 3:
            print("Вас настигла ловушка. Вы проиграли!")
            game_state["game_over"] = True
        else:
            print("Вам удалось уцелеть, но это было близко.")


def random_event(game_state):
    if pseudo_random(game_state["steps_taken"], 10) != 0:
        return

    event_type = pseudo_random(game_state["steps_taken"], 3)
    current_room = game_state["current_room"]
    room = ROOMS[current_room]

    if event_type == 0:
        print("\nВы заметили что-то блестящее на полу.")
        if "coin" not in room["items"]:
            room["items"].append("coin")
        print("Подняв монетку, вы положили её в карман.")

    elif event_type == 1:
        print("\nИз темноты послышался шорох...")
        if "sword" in game_state["player_inventory"]:
            print("Вы достали меч, и шорох прекратился. Существо отступило.")
        else:
            print("Вы затаили дыхание, пока шорох не затих.")

    elif event_type == 2:
        has_torch = "torch" in game_state["player_inventory"]
        if current_room == "trap_room" and not has_torch:
            print("\nТемнота вокруг сгустилась. Вы наступили на скрытый")
            print("механизм!")
            trigger_trap(game_state)


def describe_current_room(game_state):
    room_name = game_state["current_room"]
    room = ROOMS[room_name]

    print(f"\n== {room_name.upper()} ==")
    print(room["description"])

    if room["items"]:
        print("\nЗаметные предметы:")
        for item in room["items"]:
            print(f"  - {item}")

    if room["exits"]:
        exits_str = ", ".join(room["exits"].keys())
        print(f"\nВыходы: {exits_str}")

    if room["puzzle"] is not None:
        print("\nКажется, здесь есть загадка (используйте команду solve).")


def solve_puzzle(game_state):
    room_name = game_state["current_room"]
    room = ROOMS[room_name]

    if room["puzzle"] is None:
        print("Загадок здесь нет.")
        return

    question, correct_answer = room["puzzle"]
    print(f"\n{question}")
    user_answer = input("Ваш ответ: ").strip().lower()

    correct_variants = [correct_answer.lower()]
    if correct_answer == "10":
        correct_variants.append("десять")
    elif correct_answer == "шаг шаг шаг":
        correct_variants.append("шагшагшаг")

    if user_answer in correct_variants:
        print("Верно! Загадка решена.")
        room["puzzle"] = None

        if room_name == "hall":
            print("Сундук открылся! Внутри лежит ключ от сокровищницы.")
            if "treasure_key" not in room["items"]:
                room["items"].append("treasure_key")
        elif room_name == "library":
            print("Свиток раскрылся! Внутри указание на расположение ключа.")
        elif room_name == "trap_room":
            print("Плиты замерли. Проход безопасен.")
    else:
        print("Неверно. Попробуйте снова.")
        if room_name == "trap_room":
            trigger_trap(game_state)


def attempt_open_treasure(game_state):
    room_name = game_state["current_room"]
    room = ROOMS[room_name]

    if "treasure_chest" not in room["items"]:
        print("Сундук уже открыт.")
        return

    if "treasure_key" in game_state["player_inventory"]:
        print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
        room["items"].remove("treasure_chest")
        print("\nВ сундуке сокровище! Вы победили!")
        game_state["game_over"] = True
        return

    print("Сундук заперт. Возможно, можно открыть его кодом. Ввести код?")
    print("(да/нет)")
    choice = input("> ").strip().lower()

    if choice == "да":
        if room["puzzle"] is None:
            print("Код уже был использован ранее.")
            return

        question, correct_answer = room["puzzle"]
        print(f"\n{question}")
        user_answer = input("Ваш ответ: ").strip()

        if user_answer.lower() == correct_answer.lower():
            print("Код верный! Сундук открывается с лёгким щелчком.")
            room["items"].remove("treasure_chest")
            room["puzzle"] = None
            print("\nВ сундуке сокровище! Вы победили!")
            game_state["game_over"] = True
        else:
            print("Неверный код. Сундук остаётся запертым.")
    else:
        print("Вы отступаете от сундука.")


def show_help():
    print("\nДоступные команды:")
    for cmd, desc in COMMANDS.items():
        print(f"  {cmd:<16} - {desc}")