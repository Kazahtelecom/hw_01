"""Бенчмарк вашей реализации heap_sort против встроенной sorted()."""
import sys

# Импортируем вашу реализацию (или вставьте код функций здесь)
# from heap_sort import heap_sort 

def run_task_3():
    print("Загрузка данных (1 000 000 билетов)...")
    try:
        tickets = load_tickets("tickets_sample_1000000.csv")
    except FileNotFoundError:
        print("Ошибка: Файл tickets_sample_1000000.csv не найден!")
        return

    # Извлекаем только метки времени для сортировки
    timestamps = [t['created_time'] for t in tickets if t['created_time'] is not None]
    
    print(f"Начинаем бенчмарк для {len(timestamps)} элементов...")

    # Сравниваем
    # Используем lambda, чтобы передать копию списка, так как heap_sort меняет оригинал
    stats_heap = benchmark(lambda: heap_sort(timestamps.copy()), runs=3)
    stats_sorted = benchmark(lambda: sorted(timestamps.copy()), runs=3)

    print("\n=== Результаты эксперимента ===")
    print(f"heap_sort: {stats_heap['mean']:.3f} сек (среднее из 3 прогонов)")
    print(f"sorted():  {stats_sorted['mean']:.3f} сек (среднее из 3 прогонов)")
    
    ratio = stats_heap['mean'] / stats_sorted['mean']
    print(f"\nВывод: sorted() быстрее вашего heap_sort в {ratio:.1f} раз.")

if __name__ == "__main__":
    run_task_3()