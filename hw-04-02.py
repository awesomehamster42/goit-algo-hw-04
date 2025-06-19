from pathlib import Path

def get_cats_info(path):
    cats_info = []
    try:
        # Відкриття файлу з менеджером контексту
        with open(path, 'r', encoding='utf-8') as fh:
            lines = [line.strip() for line in fh.readlines()]    # Читаємо всі рядки та видаляємо зайві пробіли
            for line in lines:
                parts = line.split(',')    # Розділяємо кожен рядок на частини за комою
                if len(parts) == 3:    # Перевірка, чи є всі три частини (id, name, age)
                    cat = {
                        "id": parts[0],
                        "name": parts[1],
                        "age": parts[2]
                    }
                    cats_info.append(cat)    # Додаємо інформацію про кота в список

        return cats_info

    except FileNotFoundError:
        # Обробка винятку, якщо файл не знайдено
        print(f"Файл '{path}' не знайдено.")
        return None