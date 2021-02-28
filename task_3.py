from enum import Enum
import random


GAMES = 10000          # число испытаний
ROUNDS = 1000       # число исходов


class Coin(Enum):
    HEAD = 0        # орёл
    TAIL = 1        # решка


def tossing():
    return Coin(random.randint(0, 1))


def game():
    # число очков игроков
    p1 = 0     # выигрывает, когда выпадает орёл
    p2 = 0
    winning_period_p1 = 0   # период выигрывания игрока 1
    winning_period_p2 = 0
    for _ in range(ROUNDS):
        if tossing() == Coin.HEAD:
            p1 += 1
        else:
            p2 += 1
        if p1 > p2:
            winning_period_p1 += 1
        elif p2 > p1:
            winning_period_p2 += 1
    return winning_period_p1


def estimate_expected_value(sum_x, n):
    return sum_x / n


if __name__ == '__main__':
    results = {}
    for game_number in range(1, GAMES + 1):
        results[game_number] = estimate_expected_value(game(), ROUNDS)

    print(f'Оценки математических ожиданий по результатам {GAMES} игр по {ROUNDS} раундов:')
    for i in results:
        print(f'Игра {i}: {results[i]}')
