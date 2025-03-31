import os
import time

import wcwidth


def clear_previous_line() -> None:
    print("\033[F\033[K", end="")


def run_phase(seconds: int, label: str, progress_mark: str = "🔥") -> None:
    terminal_width = os.get_terminal_size().columns
    available_width = terminal_width - len(label) - 5

    mark_width = wcwidth.wcswidth(progress_mark)

    for second in range(seconds + 1):
        clear_previous_line()
        progress_fraction = second / seconds
        filled_columns = int(available_width * progress_fraction)
        count = filled_columns // mark_width if mark_width else 0
        progress_bar = progress_mark * count

        remaining_columns = available_width - wcwidth.wcswidth(progress_bar)
        progress_bar += "-" * remaining_columns

        print(f"{label}: |{progress_bar}|", flush=True)
        time.sleep(1)
