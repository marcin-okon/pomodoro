import argparse
import os
import time

from alive_progress import alive_bar


def send_notification(title: str, message: str) -> None:
    t = "-title {!r}".format(title)
    m = "-message {!r}".format(message)
    s = "-sound Hero"
    os.system("terminal-notifier {}".format(" ".join([m, t, s])))


def clear_previous_line() -> None:
    print("\033[F\033[K", end="")


def parse_args() -> dict:
    parser = argparse.ArgumentParser()
    parser.add_argument("--work-time", type=int, required=True)
    parser.add_argument("--break-time", type=int, required=True)
    parser.add_argument("--iterations", type=int, required=True)

    return vars(parser.parse_known_args()[0])


def run_phase(seconds: int, label: str) -> None:
    with alive_bar(
        seconds,
        title=f"{label}",
        elapsed=False,
        monitor=False,
        stats=False,
        bar="blocks",
        spinner=None,
        length=os.get_terminal_size().columns,
    ) as bar:
        for _ in range(seconds):
            time.sleep(1)
            bar()


def main(work_time: int, break_time: int, iterations: int) -> None:
    work_time_seconds = work_time * 60
    break_time_seconds = break_time * 60

    for i in range(1, iterations + 1):
        send_notification("Work Time", f"🍅 Iteration {i} begins now!")
        run_phase(work_time_seconds, f"🍅 Work #{i}")
        clear_previous_line()

        if i < iterations:
            send_notification("Break Time", f"☕ Take a {break_time}-minute break.")
            run_phase(break_time_seconds, f"☕ Break #{i}")
            clear_previous_line()

    send_notification("Work Done", f"Congrats, you have done {work_time * iterations} minutes of work!")


def entrypoint():
    args = parse_args()
    work_time = args["work_time"]
    break_time = args["break_time"]
    iterations = args["iterations"]

    main(work_time=work_time, break_time=break_time, iterations=iterations)
