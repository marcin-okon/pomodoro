import os
import subprocess
import time

from app import cli


def send_notification(title: str, message: str) -> None:
    args = ["terminal-notifier", "-message", message, "-title", title, "-sound", "Hero"]
    subprocess.run(args, check=True)


def clear_previous_line() -> None:
    print("\033[F\033[K", end="")


def run_phase(seconds: int, label: str) -> None:
    terminal_width = os.get_terminal_size().columns
    terminal_width_label_spaced = terminal_width - len(label) - 5
    for second in range(seconds):
        clear_previous_line()
        symbols_count = int(terminal_width_label_spaced * second // seconds)
        symbols_to_print = ("#" * symbols_count) + ((terminal_width_label_spaced - symbols_count) * "-")
        print(f"{label}: |{symbols_to_print}|")
        time.sleep(1)


def form_summary(work_time: float, break_time: float, iterations: int) -> str:
    total_work_time = work_time * iterations
    total_break_time = (break_time * iterations) if iterations > 1 else 0
    tick_code = "\u2705"
    summmary = (
        f"{tick_code * 3} \n"
        f"You accomplished {total_work_time} minutes of work, and took "
        f"{total_break_time} minutes of break. "
        f"\n{tick_code * 3}"
    )
    return summmary


def entrypoint():
    args = cli.parse_args()
    work_time = args["work"]
    break_time = args["break"]
    iterations = args["iterations"]
    work_time_seconds = int(work_time * 60)
    break_time_seconds = int(break_time * 60)

    for i in range(1, iterations + 1):
        send_notification("Work Time", f"🍅 Iteration {i} begins now!")
        run_phase(work_time_seconds, f"🍅 Work #{i}")

        if i < iterations:
            send_notification("Break Time", f"☕ Take a {break_time}-minute break.")
            run_phase(break_time_seconds, f"☕ Break #{i}")

    summary = form_summary(work_time, break_time, iterations)

    send_notification("Done!", summary)
    print(summary)
