import sys
from pathlib import Path
from colorama import Fore

def print_dir_structure(path: Path, level: int = 0) -> None:
    """
    Receive path to directory and print directory's sturcture

    Prints: 
        Directory structure
    """
    if path.exists() and path.is_dir():  
        tab = "\t" * level
        for item in path.iterdir():
            if item.is_dir():
                print(f"{Fore.RED}{tab}{item.name}/")
                print_dir_structure(item, level + 1)
            else:
                print(f"{Fore.BLUE}{tab}{item.name}")
    else:
        print("Wrong path")


dir_path = Path(sys.argv[1])
print_dir_structure(dir_path)
