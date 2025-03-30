import pytest

from app import cli


def test_minutes_input():
    assert cli.time_type("45m") == 45


def test_hours_input():
    assert cli.time_type("1h") == 60


def test_mixed_input():
    assert cli.time_type("1h15m") == 75


def test_empty_input():
    with pytest.raises(ValueError):
        cli.time_type("")


def test_zero_input():
    with pytest.raises(ValueError):
        cli.time_type("0h")


def test_malformed_input():
    with pytest.raises(ValueError):
        cli.time_type("90p")


def test_no_time_marker_input():
    assert cli.time_type("17") == 17
