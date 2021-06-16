import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from input_manager import InputManager

def print_sys_path() -> None:
    print(f"sys.path length: {len(sys.path)}")
    print(f"sys.path: {sys.path}")
    return None




def main():
    print('executing main')
    print_sys_path()

    return

def handle_cleanup():
    print('executing handle_cleanup')
    sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    print_sys_path()

if __name__ == '__main__':
    try:
        main()
    finally:
        handle_cleanup()



