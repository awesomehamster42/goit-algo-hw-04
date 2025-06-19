from pathlib import Path

def total_salary(path):
    total = 0
    try:
        # Відкриття файлу з менеджером контексту
        with open(path, 'r', encoding='utf-8') as fh:
            lines = [line.strip() for line in fh.readlines()]    # Читаємо всі рядки та видаляємо зайві пробіли
            for line in lines:
                try:
                    total += int(line.split(',')[1])    # Розділяємо рядок на дві частини(ім'я та зарплата) і додаємо значення зарплати до загальної суми
                except IndexError:
                    # Якщо рядок не містить двох частин (ім'я та зарплата), пропускаємо його
                    print("Невірний формат рядка")
                except ValueError:
                    print("Неправильне значення зарплати")
        # Перевірка якщо в файлі не було коректних даних
        if len(lines) == 0:
            print("Файл порожній.")

        avg = int(total/len(lines))     # Обчислюємо середню зарплату
        return total, avg

    except FileNotFoundError:
        # Обробка винятку, якщо файл не знайдений
        print(f"Файл '{path}' не знайдено.")
        return None