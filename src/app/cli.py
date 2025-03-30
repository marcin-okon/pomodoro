import argparse


def parse_args() -> dict:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--work", type=time_type, required=True, help="Work period duration in time format eg. 1h30m, 30m, 1h."
    )
    parser.add_argument(
        "--break", type=time_type, required=True, help="Break period duration in minutes eg. 1h30m, 30m, 1h."
    )
    parser.add_argument("--iterations", type=int, required=True, help="Number of total interations.")
    return vars(parser.parse_args())


def time_type(input: str) -> int:
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
            minutes += int(curr_frag[::-1]) * multiplier
            curr_frag = ""

    if minutes == 0:
        raise ValueError("0 minutes is not a valid input")

    return minutes
