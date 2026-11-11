import sys


def command_quest() -> None:
    print("=== Command Quest ===")
    program_name: str = sys.argv[0]
    print(f"Program name: {program_name}")

    total_args: int = len(sys.argv)

    if total_args == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {total_args - 1}")

        arg_num: int = 1
        for arg in sys.argv[1::]:
            print(f"Argument {arg_num}: {arg}")
            arg_num += 1

    print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    command_quest()