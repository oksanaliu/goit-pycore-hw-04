import sys
from pathlib import Path
from colorama import Fore, Style

def list_directory(directory, indent=""):
    try:
        for item in directory.iterdir():
            if item.is_dir():
                print(Fore.BLUE + indent + "📂 " + str(item.name))
                list_directory(item, indent + "  ")
            else:
                print(Fore.GREEN + indent + "📜 " + str(item.name))
    except PermissionError:
        print(Fore.RED + indent + "Немає доступу до директорії: " + str(directory))
    except FileNotFoundError:
        print(Fore.RED + indent + "Директорія не існує: " + str(directory))
    except Exception as e:
        print(Fore.RED + indent + "Помилка: " + str(e))

if __name__ == "__main__":
    directory_path = Path("/Users/oksanaluklan/repository/goit-pycore-hw-04/picture/picture")

    if not directory_path.is_dir():
        print("Вказаний шлях не є директорією.")

    print("Структура директорії:")
    list_directory(directory_path)