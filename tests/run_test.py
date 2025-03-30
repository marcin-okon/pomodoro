from app import run


def test_form_summary() -> None:
    assert run.form_summary(2, 2, 10) == (
        "✅✅✅\n"
        "You accomplished 20 minutes of work, and took "
        "18 minutes of break. "
        "\n✅✅✅"
    )
