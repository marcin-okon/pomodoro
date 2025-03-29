import argparse
import os
import time


def send_notification(title: str, message: str) -> None:
    t = "-title {!r}".format(title)
    m = "-message {!r}".format(message)
    s = "-sound Hero"
    os.system("terminal-notifier {}".format(" ".join([m, t, s])))


def clear_previous_line() -> None:
    print("\033[F\033[K", end="")


def parse_args() -> dict:
    parser = argparse.ArgumentParser()
    parser.add_argument("--work", type=float, required=True, help="Work period duration in minutes.")
    parser.add_argument("--break", type=float, required=True, help="Break period duration in minutes.")
    parser.add_argument("--iterations", type=int, required=True, help="Number of total interations.")

    return vars(parser.parse_known_args()[0])


def run_phase(seconds: int, label: str) -> None:
    terminal_width = os.get_terminal_size().columns
    terminal_width_label_spaced = terminal_width - len(label) - 5
    for second in range(seconds):
        clear_previous_line()
        symbols_count = int(terminal_width_label_spaced * second // seconds)
        symbols_to_print = ("#" * symbols_count) + ((terminal_width_label_spaced - symbols_count) * "-")
        print(f"{label}: |{symbols_to_print}|")
        time.sleep(1)


def entrypoint():
    args = parse_args()
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

    send_notification("Work Done", f"Congrats, you have done {work_time * iterations} minutes of work!")
