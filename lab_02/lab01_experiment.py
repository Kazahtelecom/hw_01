import time
import random


def run_experiments():
    """
    Проводит эксперименты по сравнению времени поиска элемента
    в списке (List) и во множестве (Set) при экспоненциальном
    росте размера данных (от 10^1 до 10^7 элементов).

    Результаты выводятся в консоль и сохраняются в файл 'lab01_results'.

    Notes
    -----
    Сложность поиска:
    * Список (List): O(n) - линейное время.
    * Множество (Set): O(1) - константное время.

    Расчет времени создания множества (set(data)) исключен из замера.
    """

    # name the columns
    header = f"{'Size':>30} | {'List Time (s)':>25} | {'Set Time (s)':>25} | {'Speedup':>30}"
    separator = "-" * 100

    print("--- Запуск эксперимента List vs Set ---")
    print(header)
    print(separator)


    # Открываем файл для записи
    with open("lab01_results.txt", "w", ) as f:
        f.write(header + "\n")
        f.write(separator + "\n")

        for exp in range(1, 8):

            n = 10 ** exp
            # Generate data with no occurrence of target
            data = [random.randint(1, n // 2) for _ in range(n)]
            target = -1

            # 1. Search in list (O(n))
            start = time.perf_counter()
            _ = target in data
            end = time.perf_counter()
            list_time = end - start

            # 2. Search in set (O(1))
            data_set = set(data)
            start = time.perf_counter()
            _ = target in data_set
            end = time.perf_counter()
            set_time = end - start # Exclude set creation time

            # Acceleration calculation
            speedup = list_time / set_time if set_time > 0 else 0.0

            # Format the result row
            row = f"{n:10d} | {list_time:15.6f} | {set_time:15.6f} | {speedup:10.2f}x"

            # output to console and file
            print(row)
            f.write(row + "\n")
            print(f"время поиска в списке: {list_time:.6f} с, время поиска в множестве: {set_time:.6f} с, ускорение: {speedup:.2f}x")
            print(separator)


    print("\n--- Эксперимент завершен. Результаты сохранены в 'lab01_results.txt'. ---")


if __name__ == "__main__":
    run_experiments()


