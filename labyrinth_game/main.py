from labyrinth_game.constants import ROOMS
from labyrinth_game.player_actions import (
    get_input,
    move_player,
    show_inventory,
    take_item,
    use_item,
)
from labyrinth_game.utils import (
    attempt_open_treasure,
    describe_current_room,
    show_help,
    solve_puzzle,
)

game_state = {
    'player_inventory': [],
    'current_room': 'entrance',
    'game_over': False,
    'steps_taken': 0
}


def process_command(game_state, command_line):
    if not command_line:
        return
    
    parts = command_line.split(maxsplit=1)
    cmd = parts[0].lower()
    arg = parts[1] if len(parts) > 1 else None
    
    match cmd:
        case 'go':
            if arg:
                move_player(game_state, arg.lower())
            else:
                print("Укажите направление (north/south/east/west).")
        
        case 'look':
            describe_current_room(game_state)
        
        case 'take':
            if arg:
                take_item(game_state, arg.lower())
            else:
                print("Укажите предмет для поднятия.")
        
        case 'use':
            if arg:
                use_item(game_state, arg.lower())
            else:
                print("Укажите предмет для использования.")
        
        case 'inventory' | 'inv':
            show_inventory(game_state)
        
        case 'solve':
            current_room = game_state['current_room']
            if (current_room == 'treasure_room' and
                'treasure_chest' in ROOMS[current_room]['items']):
                attempt_open_treasure(game_state)
            else:
                solve_puzzle(game_state)
        
        case 'help':
            show_help()
        
        case 'quit' | 'exit':
            print(f"\nИгра завершена. Сделано шагов: {game_state['steps_taken']}")
            game_state['game_over'] = True
        
        case _:
            print("Неизвестная команда. Введите 'help' для списка команд.")


def main():
    print("Добро пожаловать в Лабиринт сокровищ!")
    describe_current_room(game_state)
    show_help()
    
    while not game_state['game_over']:
        command = get_input()
        process_command(game_state, command)


if __name__ == "__main__":
    main()