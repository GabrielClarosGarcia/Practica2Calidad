import analysis


def mock_expenses(monkeypatch, rows):
    monkeypatch.setattr(analysis, "load_csv", lambda file_name: rows)


class TestViewExpenses:
    def test_view_expenses_path1_empty_data(self, monkeypatch, capsys):
        mock_expenses(monkeypatch, [])
        analysis.view_expenses("food", fl_name="expenses.csv", currency="Bs")
        assert "Food: 0.0 Bs" in capsys.readouterr().out

    def test_view_expenses_path2_category_match_without_month(self, monkeypatch, capsys):
        mock_expenses(monkeypatch, [
            {"Category": "food", "Month": "Jan", "Amount": "20"}
        ])
        analysis.view_expenses("food", fl_name="expenses.csv", currency="Bs")
        assert "Food: 20.0 Bs" in capsys.readouterr().out

    def test_view_expenses_path3_category_not_match_without_month(self, monkeypatch, capsys):
        mock_expenses(monkeypatch, [
            {"Category": "books", "Month": "Jan", "Amount": "20"}
        ])
        analysis.view_expenses("food", fl_name="expenses.csv", currency="Bs")
        assert "Food: 0.0 Bs" in capsys.readouterr().out

    def test_view_expenses_path4_category_and_month_match(self, monkeypatch, capsys):
        mock_expenses(monkeypatch, [
            {"Category": "food", "Month": "Feb", "Amount": "15"}
        ])
        analysis.view_expenses("food", "Feb", "expenses.csv", "Bs")
        assert "Food: 15.0 Bs" in capsys.readouterr().out

    def test_view_expenses_path5_category_not_match_with_month(self, monkeypatch, capsys):
        mock_expenses(monkeypatch, [
            {"Category": "books", "Month": "Feb", "Amount": "15"}
        ])
        analysis.view_expenses("food", "Feb", "expenses.csv", "Bs")
        assert "Food: 0.0 Bs" in capsys.readouterr().out

    def test_view_expenses_path6_month_not_match(self, monkeypatch, capsys):
        mock_expenses(monkeypatch, [
            {"Category": "food", "Month": "Jan", "Amount": "15"}
        ])
        analysis.view_expenses("food", "Feb", "expenses.csv", "Bs")
        assert "Food: 0.0 Bs" in capsys.readouterr().out

    def test_view_expenses_path7_multiple_rows(self, monkeypatch, capsys):
        mock_expenses(monkeypatch, [
            {"Category": "food", "Month": "Jan", "Amount": "10"},
            {"Category": "books", "Month": "Jan", "Amount": "25"},
            {"Category": "food", "Month": "Feb", "Amount": "50"},
            {"Category": "food", "Month": "Jan", "Amount": "2.5"},
        ])
        analysis.view_expenses("food", "Jan", "expenses.csv", "Bs")
        assert "Food: 12.5 Bs" in capsys.readouterr().out


class TestSummary:
    def test_summary_path1_empty_data(self, monkeypatch, capsys):
        mock_expenses(monkeypatch, [])
        analysis.summary("expenses.csv", "Bs")
        assert capsys.readouterr().out.strip() == "Total spent: 0.0 Bs"

    def test_summary_path2_one_category(self, monkeypatch, capsys):
        mock_expenses(monkeypatch, [
            {"Category": "food", "Amount": "20"}
        ])
        analysis.summary("expenses.csv", "Bs")
        assert capsys.readouterr().out.splitlines() == [
            "Total spent: 20.0 Bs",
            "Total spent on food: 20.0 Bs"
        ]

    def test_summary_path3_multiple_categories(self, monkeypatch, capsys):
        mock_expenses(monkeypatch, [
            {"Category": "food", "Amount": "10"},
            {"Category": "books", "Amount": "5"},
            {"Category": "food", "Amount": "2.5"},
        ])
        analysis.summary("expenses.csv", "Bs")
        assert capsys.readouterr().out.splitlines() == [
            "Total spent: 17.5 Bs",
            "Total spent on food: 12.5 Bs",
            "Total spent on books: 5.0 Bs"
        ]