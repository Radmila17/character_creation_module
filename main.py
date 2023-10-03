from random import randint


def attack(char_name, char_class):
    damages = {
        'warrior': 5 + randint(3, 5),
        'mage': 5 + randint(5, 10),
        'healer': 5 + randint(-3, -1),
    }
    return f'{char_name} нанёс урон противнику равный {damages[char_class]}'


def defence(char_name, char_class):
    block_damages = {
        'warrior': 10 + randint(5, 10),
        'mage': 10 + randint(-2, 2),
        'healer': 10 + randint(2, 5),
    }
    return f'{char_name} блокировал {block_damages[char_class]} урона'


def special(char_name, char_class):
    skills = {
        'warrior': (f'«Выносливость {80 + 25}»'),
        'mage': (f'«Атака {5 + 40}»'),
        'healer': (f'«Защита {10 + 30}»'),
    }
    return f'{char_name} применил специальное умение {skills[char_class]}'


def start_training(char_name, char_class):
    char_identifications = {
        'warrior': 'Воитель — отличный боец ближнего боя.',
        'mage': 'Маг — превосходный укротитель стихий.',
        'healer': 'Лекарь — чародей, способный исцелять раны.',
    }
    print(f'{char_name}, ты {char_identifications[char_class]}'),
    print(
        'Потренируйся управлять своими навыками. '
        'Введи одну из команд: '
        'attack — чтобы атаковать противника, '
        'defence — чтобы блокировать атаку противника или '
        'special — чтобы использовать свою суперсилу. '
        'Если не хочешь тренироваться, введи команду skip.'
    )
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        commands = {
            'attack': attack(char_name, char_class),
            'defence': defence(char_name, char_class),
            'special': special(char_name, char_class),
        }
        if cmd != 'skip':
            print(commands[cmd])
    return 'Тренировка окончена.'


def choice_char_class():
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input(
            'Введи название персонажа, '
            'за которого хочешь играть: '
            'Воитель — warrior, '
            'Маг — mage, '
            'Лекарь — healer: '
        )
        char_descriptions = {
            'warrior': (
                'Воитель — дерзкий воин ближнего боя. '
                'Сильный, выносливый и отважный.'
            ),
            'mage': (
                'Маг — находчивый воин дальнего боя. '
                'Обладает высоким интеллектом.'
            ),
            'healer': (
                'Лекарь — могущественный заклинатель. '
                'Черпает силы из природы, веры и духов.'
            ),
        }
        print(char_descriptions[char_class])
        approve_choice = input(
            'Нажми (Y), чтобы подтвердить выбор, или любую другую кнопку, '
            'чтобы выбрать другого персонажа '
        ).lower()
    return char_class


def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))


main()
