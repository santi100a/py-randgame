def clear():
    print('\033[2J\033[1;1H', end='')
    from os import system, name
    system('cls' if name == 'nt' else 'clear')