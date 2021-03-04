import random

CYLINDER_DIAM_MU = 1            # мат ожидание диаметра цилиндра
CYLINDER_DIAM_SIGMA = 0.01      # стандартное отклонение диаметра цилиндра
ROD_DIAM_MU = 0.99              # мат ожидание диаметра стержня
ROD_DIAM_SIGMA = 0.01           # стандартное отклонение диаметра стержня
NUMBER_OF_PAIRS = 1000          # число цилиндров и стержней

if __name__ == '__main__':
    defective_pairs = 0
    for _ in range(NUMBER_OF_PAIRS):
        cyl_d = random.gauss(CYLINDER_DIAM_MU, CYLINDER_DIAM_SIGMA)
        rod_d = random.gauss(ROD_DIAM_MU, ROD_DIAM_SIGMA)
        if cyl_d < rod_d:
            defective_pairs += 1
    print(f'Из {NUMBER_OF_PAIRS} пар дефектыми оказались {defective_pairs}\n')
    print(f'Процент дефектных пар: {(defective_pairs/NUMBER_OF_PAIRS)*100}%')
