import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)  # Автоматичне скидання кольору після виводу

def sort_key(path: Path):
    # ім'я в нижньому регістрі
    return path.name.lower()

def print_tree(path: Path, indent=''):
    # Обробка винятків
    try:
        items = sorted(path.iterdir(), key=sort_key)
    except NotADirectoryError:
        print(Fore.RED + f" Шлях не є директорією: {path}" + Style.RESET_ALL)
        return
    except FileNotFoundError:
        print(Fore.RED + f" Шлях не існує: {path}" + Style.RESET_ALL)
        return
    except PermissionError:
        print(Fore.RED + f" Немає доступу до: {path}" + Style.RESET_ALL)
        return

    # Візуалізація дерева файлової структури
    for item in items:
        if item.is_dir():
            print(indent + Fore.BLUE + item.name + '/' + Style.RESET_ALL)
            print_tree(item, indent + '    ')
        else:
            print(indent + Fore.GREEN + item.name + Style.RESET_ALL)


# Основний блок, який виконується при запуску скрипта
if __name__ == '__main__':
    try:
        directory_path = Path(sys.argv[1])
    except IndexError:
        print("Вкажіть шлях до директорії як аргумент при запуску.")
        print("Приклад: python hw-04-03.py /шлях/до/директорії")
        sys.exit(1)

    print(f"Структура директорії: {directory_path}")
    print_tree(directory_path)