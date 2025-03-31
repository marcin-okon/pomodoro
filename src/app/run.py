import subprocess

from app import cli, progress_bar


def send_notification(title: str, message: str, sound: str = "Hero") -> None:
    args = [
        "terminal-notifier",
        "-message",
        message,
        "-title",
        title,
        "-sound",
        sound,
    ]
    subprocess.run(args, check=True)


def form_summary(work_time: float, break_time: float, iterations: int) -> str:
    total_work_time = work_time * iterations
    total_break_time = break_time * (iterations - 1)
    summmary = (
        "✅✅✅\n"
        f"You accomplished {total_work_time} minutes of work, and took "
        f"{total_break_time} minutes of break. "
        "\n✅✅✅"
    )
    return summmary


def entrypoint() -> None:
    args = cli.parse_args()
    work_time = args["work"]
    break_time = args["break"]
    iterations = args["iterations"]
    progress_mark = args["progress_mark"]
    notification_sound = args["notification_sound"]
    work_time_seconds = int(work_time * 60)
    break_time_seconds = int(break_time * 60)

    for i in range(1, iterations + 1):
        send_notification(
            "Work Time", f"🍅 Iteration {i} begins now!", notification_sound
        )
        progress_bar.run_phase(
            work_time_seconds, f"🍅 Work #{i}", progress_mark
        )

        if i < iterations:
            send_notification(
                "Break Time",
                f"☕ Take a {break_time}-minute break.",
                notification_sound,
            )
            progress_bar.run_phase(
                break_time_seconds, f"☕ Break #{i}", progress_mark
            )

    summary = form_summary(work_time, break_time, iterations)

    send_notification("Done!", summary, notification_sound)
    print(summary)
