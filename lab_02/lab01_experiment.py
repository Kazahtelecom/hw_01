import time
import random
from typing import Tuple 


def run_experiments(n: int) -> Tuple[float, float]:  
    """
    Генерирует данные размера n и замеряет время поиска.
    Используется наихудший случай (элемента нет в списке).

    Args:
        n (int): Размер данных.

    Returns:
        tuple: (время_список, время_множество)
    """
    # Генерация данных
    data = [random.randint(1, n // 2) for _ in range(n)]
    target = -1  # Элемента точно нет -> наихудший случай для списка

    # 1. Замер списка
    start = time.perf_counter()
    _ = target in data
    t_list = time.perf_counter() - start

    # 2. Замер множества (время создания не учитываем)
    data_set = set(data)
    start = time.perf_counter()
    _ = target in data_set
    t_set = time.perf_counter() - start

    return t_list, t_set


def logs(f, n:int,
         t_list:float,
         t_set:float
        ) -> None:
    """
    Рассчитывает ускорение и записывает строку результатов 
    в файл и в консоль.

    Args:
        f (file object): Открытый файл для записи.
        n (int): Размер данных.
        t_list (float): Время поиска в списке.
        t_set (float): Время поиска в множестве.
    """
    # Считаем ускорение
    speedup = t_list / t_set if t_set > 0 else 0.0

    # Форматируем строку (используем f-строки для красоты)
    # <10 означает выравнивание по левому краю, ширина 10
    row = f"{n:<10} | {t_list:<15.6f} | {t_set:<15.6f} | {speedup:<10.1f}x"

    # Печатаем в терминал
    print(row)

    # Пишем в файл (+ перенос строки \n)
    f.write(row + "\n")


def benchmark() -> None:
    """
    Основная функция. Настраивает файл, запускает цикл по размерам
    и вызывает функции эксперимента и логирования.
    """
    filename = 'lab01_results.txt'

    # Заголовки таблицы
    header = f"{'Размер':<10} | {'Список (сек)':<15} | {'Множество (сек)':<15} | {'Ускорение':<10}"
    separator = "-" * 65

    print("--- Start Benchmark ---")
    print(header)
    print(separator)

    # Открываем файл один раз перед циклом
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(header + "\n")
        f.write(separator + "\n")

        # Цикл по степеням десятки: 10, 100, ..., 10,000,000
        for exp in range(1, 8):
            n = 10 ** exp

            # 1. Запускаем эксперимент
            t_list, t_set = run_experiments(n)

            # 2. Логируем результаты
            logs(f, n, t_list, t_set)

    print(f"\nРезультаты сохранены в {filename}")


if __name__ == "__main__":
    benchmark()
