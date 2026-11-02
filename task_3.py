from pathlib import Path
import sys

from colorama import Fore, Style, init


def display_tree(directory, prefix=""):
    entries = sorted(
        directory.iterdir(), key=lambda item: (not item.is_dir(), item.name.casefold())
    )
    for index, entry in enumerate(entries):
        last = index == len(entries) - 1
        connector = "└── " if last else "├── "
        color = Fore.CYAN if entry.is_dir() else Fore.GREEN
        marker = " -> symlink" if entry.is_symlink() else ""
        print(f"{prefix}{connector}{color}{entry.name}{marker}{Style.RESET_ALL}")
        if entry.is_dir() and not entry.is_symlink():
            extension = "    " if last else "│   "
            try:
                display_tree(entry, prefix + extension)
            except OSError as error:
                print(f"{prefix}{extension}{Fore.RED}{error}{Style.RESET_ALL}")


def main():
    init()
    if len(sys.argv) != 2:
        print("Usage: python task_3.py <directory>")
        return 1
    try:
        directory = Path(sys.argv[1]).expanduser()
        if not directory.exists():
            print("The path does not exist.")
            return 1
        if not directory.is_dir():
            print("The path is not a directory.")
            return 1
        print(f"{Fore.CYAN}{directory.resolve()}{Style.RESET_ALL}")
        display_tree(directory)
    except OSError as error:
        print(f"Cannot access the directory: {error}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
