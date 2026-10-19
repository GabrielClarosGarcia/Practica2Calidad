import sys
from unittest.mock import patch
import pytest

from expense_tracker import (
    cmd_process,
    no_command,
    NoCommand,
    check_argumets_count,
    MissingArguments,
    TooManyArguments,
    InvalidPrice,
    InvalidCategory,
    InvalidMonthName,
    WrongConfigChange,
    UnknownCommand,
)


def test_no_command_raises_exception(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["expense_tracker.py"])
    with pytest.raises(NoCommand):
        no_command()


def test_no_command_with_command(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["expense_tracker.py", "summary"])
    assert no_command() is None


def test_check_arguments_count_missing(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["expense_tracker.py"])
    with pytest.raises(MissingArguments):
        check_argumets_count("summary")


def test_check_arguments_count_too_many(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["expense_tracker.py", "summary", "extra"])
    with pytest.raises(TooManyArguments):
        check_argumets_count("summary")


def test_check_arguments_count_valid(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["expense_tracker.py", "summary"])
    assert check_argumets_count("summary") is None


class TestCmdProcess:
    @patch("expense_tracker.configure", return_value={"datafile": "test.csv", "currency": "$"})
    @patch("expense_tracker.add_expense")
    def test_cmd_process_add_with_note(self, mock_add, mock_conf, monkeypatch):
        monkeypatch.setattr(
            sys, "argv", ["expense_tracker.py", "add", "March", "50", "food", "Lunch"]
        )
        cmd_process()
        mock_add.assert_called_once_with("Mar", "50", "food", "lunch", file_name="test.csv")

    @patch("expense_tracker.configure", return_value={"datafile": "test.csv", "currency": "$"})
    @patch("expense_tracker.add_expense")
    def test_cmd_process_add_without_note_numeric_month(self, mock_add, mock_conf, monkeypatch):
        monkeypatch.setattr(
            sys, "argv", ["expense_tracker.py", "add", "3", "25.5", "entertainment"]
        )
        cmd_process()
        mock_add.assert_called_once_with("Mar", "25.5", "entertainment", None, file_name="test.csv")

    @patch("expense_tracker.configure", return_value={"datafile": "test.csv", "currency": "$"})
    def test_cmd_process_add_invalid_price(self, mock_conf, monkeypatch):
        monkeypatch.setattr(
            sys, "argv", ["expense_tracker.py", "add", "March", "not_a_number", "food"]
        )
        with pytest.raises(InvalidPrice):
            cmd_process()

    @patch("expense_tracker.configure", return_value={"datafile": "test.csv", "currency": "$"})
    def test_cmd_process_add_invalid_category(self, mock_conf, monkeypatch):
        monkeypatch.setattr(
            sys, "argv", ["expense_tracker.py", "add", "March", "50", "123"]
        )
        with pytest.raises(InvalidCategory):
            cmd_process()

    @patch("expense_tracker.configure", return_value={"datafile": "test.csv", "currency": "$"})
    def test_cmd_process_add_invalid_month(self, mock_conf, monkeypatch):
        monkeypatch.setattr(
            sys, "argv", ["expense_tracker.py", "add", "NotAMonth", "50", "food"]
        )
        with pytest.raises(InvalidMonthName):
            cmd_process()

    @patch("expense_tracker.configure", return_value={"datafile": "test.csv", "currency": "$"})
    @patch("expense_tracker.view_expenses")
    def test_cmd_process_view_with_month(self, mock_view, mock_conf, monkeypatch):
        monkeypatch.setattr(
            sys, "argv", ["expense_tracker.py", "view", "food", "October"]
        )
        cmd_process()
        mock_view.assert_called_once_with(
            "food", month_name="Oct", fl_name="test.csv", currency="$"
        )

    @patch("expense_tracker.configure", return_value={"datafile": "test.csv", "currency": "$"})
    @patch("expense_tracker.view_expenses")
    def test_cmd_process_view_without_month(self, mock_view, mock_conf, monkeypatch):
        monkeypatch.setattr(
            sys, "argv", ["expense_tracker.py", "view", "food"]
        )
        cmd_process()
        mock_view.assert_called_once_with(
            "food", month_name=None, fl_name="test.csv", currency="$"
        )

    @patch("expense_tracker.configure", return_value={"datafile": "test.csv", "currency": "$"})
    def test_cmd_process_view_invalid_category(self, mock_conf, monkeypatch):
        monkeypatch.setattr(
            sys, "argv", ["expense_tracker.py", "view", "January"]
        )
        with pytest.raises(InvalidCategory):
            cmd_process()

    @patch("expense_tracker.configure", return_value={"datafile": "test.csv", "currency": "$"})
    def test_cmd_process_view_invalid_month(self, mock_conf, monkeypatch):
        monkeypatch.setattr(
            sys, "argv", ["expense_tracker.py", "view", "food", "InvalidMonth"]
        )
        with pytest.raises(InvalidMonthName):
            cmd_process()

    @patch("expense_tracker.configure", return_value={"datafile": "test.csv", "currency": "$"})
    @patch("expense_tracker.summary")
    def test_cmd_process_summary(self, mock_summary, mock_conf, monkeypatch):
        monkeypatch.setattr(
            sys, "argv", ["expense_tracker.py", "summary"]
        )
        cmd_process()
        mock_summary.assert_called_once_with(fl_name="test.csv", currency="$")

    @patch("expense_tracker.configure", return_value={"datafile": "test.csv", "currency": "$"})
    @patch("expense_tracker.chart")
    def test_cmd_process_chart(self, mock_chart, mock_conf, monkeypatch):
        monkeypatch.setattr(
            sys, "argv", ["expense_tracker.py", "chart"]
        )
        cmd_process()
        mock_chart.assert_called_once_with(file_name="test.csv")

    @patch("expense_tracker.configure", return_value={"datafile": "test.csv", "currency": "$"})
    @patch("expense_tracker.change_setting", return_value=True)
    def test_cmd_process_config_success(self, mock_change, mock_conf, monkeypatch, capsys):
        monkeypatch.setattr(
            sys, "argv", ["expense_tracker.py", "config", "currency", "EUR"]
        )
        cmd_process()
        mock_change.assert_called_once_with("currency", "EUR")
        captured = capsys.readouterr()
        assert "currency successfully changed to EUR" in captured.out

    @patch("expense_tracker.configure", return_value={"datafile": "test.csv", "currency": "$"})
    @patch("expense_tracker.change_setting", return_value=False)
    def test_cmd_process_config_failure(self, mock_change, mock_conf, monkeypatch):
        monkeypatch.setattr(
            sys, "argv", ["expense_tracker.py", "config", "wrong_key", "val"]
        )
        with pytest.raises(WrongConfigChange):
            cmd_process()

    @pytest.mark.parametrize("flag", ["help", "--help", "-h"])
    @patch("expense_tracker.configure", return_value={"datafile": "test.csv", "currency": "$"})
    def test_cmd_process_help(self, mock_conf, monkeypatch, capsys, flag):
        monkeypatch.setattr(
            sys, "argv", ["expense_tracker.py", flag]
        )
        cmd_process()
        captured = capsys.readouterr()
        assert "Usage:" in captured.out

    @patch("expense_tracker.configure", return_value={"datafile": "test.csv", "currency": "$"})
    def test_cmd_process_unknown_command(self, mock_conf, monkeypatch):
        monkeypatch.setattr(
            sys, "argv", ["expense_tracker.py", "inventado"]
        )
        with pytest.raises(UnknownCommand):
            cmd_process()
