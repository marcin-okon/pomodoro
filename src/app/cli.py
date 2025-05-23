import argparse
from typing import Any


def parse_args() -> dict[str, Any]:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--work",
        type=time_type,
        required=True,
        help="Work period duration in time format eg. 1h30m, 30m, 1h.",
    )
    parser.add_argument(
        "--break",
        type=time_type,
        required=True,
        help="Break period duration in minutes eg. 1h30m, 30m, 1h.",
    )
    parser.add_argument(
        "--iterations",
        type=int,
        required=True,
        help="Number of total interations.",
    )
    parser.add_argument(
        "--progress-mark",
        type=progress_mark_type,
        required=False,
        default="🔥",
        help="Symbol showed on the progress bar",
    )
    parser.add_argument(
        "--notification-sound",
        type=str,
        choices=[
            "Basso",
            "Blow",
            "Bottle",
            "Frog",
            "Funk",
            "Glass",
            "Hero",
            "Morse",
            "Ping",
            "Pop",
            "Purr",
            "Sosumi",
            "Submarine",
            "Tink",
        ],
        required=False,
        default="Hero",
    )
    return vars(parser.parse_args())


def iterations_type(input: int) -> int:
    if input < 0:
        raise ValueError("Number of iterations cannot be negative.")
    return input


def time_type(input: str) -> int:
    if "hm" in input or "mh" in input:
        raise ValueError("Invalid Input")

    if input in ["h", "m"]:
        raise ValueError("Invalid Input")

    if any(i not in "0123456789hm" for i in input):
        raise ValueError("Invalid format of the input")

    if not input:
        raise ValueError("Input cannot be empty")

    input = input.lower()
    minutes = 0
    stack = list(input)
    multiplier = 1
    curr_frag = ""
    while stack:
        el = stack.pop()
        if el == "h":
            multiplier = 60
        elif el == "m":
            multiplier = 1
        else:
            curr_frag = curr_frag + el
            while stack and stack[-1] not in "hm":
                curr_frag += stack.pop()
            curr_minutes = int(curr_frag[::-1])

            if multiplier == 1 and curr_minutes > 59:
                raise ValueError("Minutes exceed 59.")

            minutes += int(curr_frag[::-1]) * multiplier
            curr_frag = ""

    if minutes == 0:
        raise ValueError("0 minutes is not a valid input")

    return minutes


def progress_mark_type(input: str) -> str:
    if len(input) > 5:
        raise ValueError("Length of the progressMark cannot exceed 5")
    return input
