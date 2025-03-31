import pytest

from app import cli


def test_minutes_input() -> None:
    assert cli.time_type("45m") == 45


def test_hours_input() -> None:
    assert cli.time_type("1h") == 60


def test_mixed_input() -> None:
    assert cli.time_type("1h15m") == 75


def test_empty_input() -> None:
    with pytest.raises(ValueError):
        cli.time_type("")


def test_zero_input() -> None:
    with pytest.raises(ValueError):
        cli.time_type("0h")


def test_malformed_input() -> None:
    with pytest.raises(ValueError):
        cli.time_type("90p")


def test_no_time_marker_input() -> None:
    assert cli.time_type("17") == 17


def test_minutes_over_59_input() -> None:
    with pytest.raises(ValueError):
        cli.time_type("1h90m")


def test_iteration_input_valid() -> None:
    assert cli.iterations_type(7) == 7


def test_iteration_input_negative() -> None:
    with pytest.raises(ValueError):
        cli.iterations_type(-1)


def test_progress_mark_valid_len() -> None:
    assert cli.progress_mark_type("$%#") == "$%#"


def test_progress_mark_invalid_len() -> None:
    with pytest.raises(ValueError):
        cli.progress_mark_type("MMMMMMMMMMMMMM")
