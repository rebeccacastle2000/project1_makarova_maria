from labyrinth_game.constants import ROOMS


def describe_current_room(game_state):
    room_name = game_state['current_room']
    room = ROOMS[room_name]
    
    print(f"\n== {room_name.upper()} ==")
    print(room['description'])
    
    if room['items']:
        print("\nЗаметные предметы:")
        for item in room['items']:
            print(f"  - {item}")
    
    if room['exits']:
        exits_str = ', '.join(room['exits'].keys())
        print(f"\nВыходы: {exits_str}")
    
    if room['puzzle'] is not None:
        print("\nКажется, здесь есть загадка (используйте команду solve).")


def solve_puzzle(game_state):
    room_name = game_state['current_room']
    room = ROOMS[room_name]
    
    if room['puzzle'] is None:
        print("Загадок здесь нет.")
        return
    
    question, correct_answer = room['puzzle']
    print(f"\n{question}")
    user_answer = input("Ваш ответ: ").strip()
    
    if user_answer.lower() == correct_answer.lower():
        print("Верно! Загадка решена.")
        room['puzzle'] = None
        
        if room_name == 'hall':
            print("Сундук открылся! Внутри лежит ключ от сокровищницы.")
            if 'treasure_key' not in room['items']:
                room['items'].append('treasure_key')
        elif room_name == 'library':
            print("Свиток раскрылся! Внутри указание на расположение ключа.")
        elif room_name == 'trap_room':
            print("Плиты замерли. Проход безопасен.")
    else:
        print("Неверно. Попробуйте снова.")


def attempt_open_treasure(game_state):
    room_name = game_state['current_room']
    room = ROOMS[room_name]
    
    if 'treasure_chest' not in room['items']:
        print("Сундук уже открыт.")
        return
    
    if 'treasure_key' in game_state['player_inventory']:
        print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
        room['items'].remove('treasure_chest')
        print("\nВ сундуке сокровище! Вы победили!")
        game_state['game_over'] = True
        return
    
    print("Сундук заперт. Возможно, можно открыть его кодом. Ввести код? (да/нет)")
    choice = input("> ").strip().lower()
    
    if choice == 'да':
        if room['puzzle'] is None:
            print("Код уже был использован ранее.")
            return
        
        question, correct_answer = room['puzzle']
        print(f"\n{question}")
        user_answer = input("Ваш ответ: ").strip()
        
        if user_answer.lower() == correct_answer.lower():
            print("Код верный! Сундук открывается с лёгким щелчком.")
            room['items'].remove('treasure_chest')
            room['puzzle'] = None
            print("\nВ сундуке сокровище! Вы победили!")
            game_state['game_over'] = True
        else:
            print("Неверный код. Сундук остаётся запертым.")
    else:
        print("Вы отступаете от сундука.")

def show_help():
    print("\nДоступные команды:")
    print("  go <direction>  - перейти в направлении (north/south/east/west)")
    print("  look            - осмотреть текущую комнату")
    print("  take <item>     - поднять предмет")
    print("  use <item>      - использовать предмет из инвентаря")
    print("  inventory       - показать инвентарь")
    print("  solve           - попытаться решить загадку в комнате")
    print("  quit            - выйти из игры")
    print("  help            - показать это сообщение") 