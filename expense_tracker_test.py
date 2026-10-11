import sys
import pytest

from expense_tracker import (
    no_command,
    NoCommand,
    check_argumets_count,
    MissingArguments,
    TooManyArguments,
)


# ==========================================
# Tests de la función no_command()
# ==========================================

def test_no_command_raises_exception(monkeypatch):
    # Camino donde no se proporciona ningún comando.
    monkeypatch.setattr(
        sys,
        "argv",
        ["expense_tracker.py"]
    )

    with pytest.raises(NoCommand):
        no_command()


def test_no_command_with_command(monkeypatch):
    # Camino donde sí existe al menos un comando.
    monkeypatch.setattr(
        sys,
        "argv",
        ["expense_tracker.py", "summary"]
    )

    result = no_command()

    assert result is None

# ==========================================
# Tests de la función check_argumets_count()
# ==========================================

def test_check_arguments_count_missing(monkeypatch):
    # Camino donde hay menos argumentos de los requeridos.
    monkeypatch.setattr(
        sys,
        "argv",
        ["expense_tracker.py"]
    )

    with pytest.raises(MissingArguments):
        check_argumets_count("summary")


def test_check_arguments_count_too_many(monkeypatch):
    # Camino donde hay más argumentos de los permitidos.
    monkeypatch.setattr(
        sys,
        "argv",
        ["expense_tracker.py", "summary", "extra"]
    )

    with pytest.raises(TooManyArguments):
        check_argumets_count("summary")


def test_check_arguments_count_valid(monkeypatch):
    # Camino donde la cantidad de argumentos es válida.
    monkeypatch.setattr(
        sys,
        "argv",
        ["expense_tracker.py", "summary"]
    )

    result = check_argumets_count("summary")

    assert result is None