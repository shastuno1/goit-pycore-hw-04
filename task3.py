import sys
from pathlib import Path
from colorama import init, Fore, Style

# ініціалізуємо colorama
init(autoreset=True)


def print_directory_structure(path: Path, indent: str = ""):
    try:
        for item in path.iterdir():
            if item.is_dir():
                # директорії — сині
                print(indent + Fore.BLUE + f"📂 {item.name}")
                print_directory_structure(item, indent + "   ")
            else:
                # файли — зелені
                print(indent + Fore.GREEN + f"📜 {item.name}")
    except PermissionError:
        print(indent + Fore.RED + "Немає доступу до папки")


def main():
    # перевірка аргументу
    if len(sys.argv) < 2:
        print(Fore.RED + "Вкажіть шлях до директорії!")
        return

    directory_path = Path(sys.argv[1])

    # перевірка що шлях існує
    if not directory_path.exists():
        print(Fore.RED + "Такий шлях не існує!")
        return

    # перевірка що це директорія
    if not directory_path.is_dir():
        print(Fore.RED + "Це не директорія!")
        return

    print(Fore.YELLOW + f"📦 {directory_path.name}")
    print_directory_structure(directory_path)


if __name__ == "__main__":
    main()
