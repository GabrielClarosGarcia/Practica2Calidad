from unittest.mock import MagicMock
import visualization


def mock_chart(monkeypatch, rows):
    pie_ax = MagicMock()
    bar_ax = MagicMock()
    subplot = MagicMock(return_value=(MagicMock(), (pie_ax, bar_ax)))
    show = MagicMock()
    tight_layout = MagicMock()

    monkeypatch.setattr(visualization, "load_csv", lambda file_name: rows)
    monkeypatch.setattr(visualization.plt, "subplots", subplot)
    monkeypatch.setattr(visualization.plt, "show", show)
    monkeypatch.setattr(visualization.plt, "tight_layout", tight_layout)

    return pie_ax, bar_ax, subplot, show, tight_layout


class TestChart:
    def test_chart_path1_empty_data(self, monkeypatch):
        pie, bar, _, show, _ = mock_chart(monkeypatch, [])
        visualization.chart("expenses.csv")
        pie.pie.assert_called_once_with(
            [], labels=[], shadow=True, autopct="%1.2f%%"
        )
        bar.bar.assert_called_once_with([], [])
        show.assert_called_once()

    def test_chart_path2_one_expense(self, monkeypatch):
        pie, bar, _, _, _ = mock_chart(monkeypatch, [
            {"Category": "food", "Month": "Jan", "Amount": "10"}
        ])
        visualization.chart("expenses.csv")
        pie.pie.assert_called_once_with(
            [10.0], labels=["food"], shadow=True, autopct="%1.2f%%"
        )
        bar.bar.assert_called_once_with(["Jan"], [10.0])

    def test_chart_path3_multiple_expenses(self, monkeypatch):
        pie, bar, _, _, _ = mock_chart(monkeypatch, [
            {"Category": "food", "Month": "Mar", "Amount": "15"},
            {"Category": "books", "Month": "Jan", "Amount": "8"},
            {"Category": "food", "Month": "Jan", "Amount": "5"},
        ])
        visualization.chart("expenses.csv")
        pie.pie.assert_called_once_with(
            [20.0, 8.0], labels=["food", "books"],
            shadow=True, autopct="%1.2f%%"
        )
        bar.bar.assert_called_once_with(["Jan", "Mar"], [13.0, 15.0])

    def test_chart_path4_chart_configuration(self, monkeypatch):
        pie, bar, subplot, show, tight_layout = mock_chart(monkeypatch, [
            {"Category": "food", "Month": "Jan", "Amount": "10"}
        ])
        visualization.chart("expenses.csv")
        subplot.assert_called_once_with(1, 2, figsize=(10, 5))
        pie.legend.assert_called_once_with(title="Categories:")
        pie.set_title.assert_called_once_with("Category Costs")
        pie.axis.assert_called_once_with("equal")
        bar.set_title.assert_called_once_with("Monthly Costs")
        bar.set_xlabel.assert_called_once_with("Months")
        bar.set_ylabel.assert_called_once_with("Total Costs")
        tight_layout.assert_called_once()
        show.assert_called_once()