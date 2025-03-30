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
