import os
import time


def clear_previous_line() -> None:
    print("\033[F\033[K", end="")


def run_phase(seconds: int, label: str, progress_mark: str = "#") -> None:
    terminal_width = os.get_terminal_size().columns
    terminal_width_label_spaced = terminal_width - len(label) - 5
    for second in range(seconds):
        clear_previous_line()
        symbols_count = int(terminal_width_label_spaced * second // seconds)
        symbols_to_print = (progress_mark * symbols_count) + (
            (terminal_width_label_spaced - symbols_count) * "-"
        )
        print(f"{label}: |{symbols_to_print}|")
        time.sleep(1)
