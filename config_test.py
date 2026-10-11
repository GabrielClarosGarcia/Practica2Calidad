from config import (
    is_file_exist,
    create_default_data,
    load_conf,
    configure,
    change_setting,
    check_file_name,
    write_changes,
)

# ==========================================
# Tests de la función is_file_exist()
# ==========================================

def test_is_file_exist_true(monkeypatch):
    # Este test pertenece a la función is_file_exist().
    # Verifica el camino donde setting.json sí existe.
    monkeypatch.setattr("config.listdir", lambda: ["setting.json"])

    assert is_file_exist() is True


def test_is_file_exist_false(monkeypatch):
    # Este test pertenece a la función is_file_exist().
    # Verifica el camino donde setting.json no existe.
    monkeypatch.setattr("config.listdir", lambda: [])

    assert is_file_exist() is False


# ==========================================
# Test de la función create_default_data()
# ==========================================

def test_create_default_data(tmp_path, monkeypatch):
    # Este test pertenece a la función create_default_data().
    # Verifica que se cree setting.json y que se retornen
    # correctamente los valores por defecto.
    monkeypatch.chdir(tmp_path)

    result = create_default_data()

    assert result == {
        "currency": "Reals",
        "datafile": "expense.csv",
    }

    assert (tmp_path / "setting.json").exists()


# ==========================================
# Test de la función load_conf()
# ==========================================

def test_load_conf(tmp_path, monkeypatch):
    # Este test pertenece a la función load_conf().
    # Verifica que se pueda leer correctamente un setting.json
    # existente y retornar su contenido como diccionario.
    monkeypatch.chdir(tmp_path)

    setting_file = tmp_path / "setting.json"
    setting_file.write_text(
        '{"currency": "USD", "datafile": "expenses.csv"}',
        encoding="utf-8"
    )

    result = load_conf()

    assert result == {
        "currency": "USD",
        "datafile": "expenses.csv",
    }


# ==========================================
# Tests de la función configure()
# ==========================================

def test_configure_load_existing(monkeypatch):
    # Este test pertenece a la función configure().
    # Verifica el camino donde el archivo setting.json existe
    # y configure() debe utilizar load_conf().
    expected = {
        "currency": "USD",
        "datafile": "expenses.csv",
    }

    monkeypatch.setattr("config.is_file_exist", lambda: True)
    monkeypatch.setattr("config.load_conf", lambda: expected)

    result = configure()

    assert result == expected


def test_configure_create_default(monkeypatch):
    # Este test pertenece a la función configure().
    # Verifica el camino donde setting.json no existe
    # y configure() debe utilizar create_default_data().
    expected = {
        "currency": "Reals",
        "datafile": "expense.csv",
    }

    monkeypatch.setattr("config.is_file_exist", lambda: False)
    monkeypatch.setattr("config.create_default_data", lambda: expected)

    result = configure()

    assert result == expected

# ==========================================
# Tests de la función change_setting()
# ==========================================

def test_change_setting_currency(monkeypatch):
    # Camino: parámetro currency válido.
    setting = {
        "currency": "Reals",
        "datafile": "expense.csv",
    }

    written = {}

    monkeypatch.setattr("config.configure", lambda: setting.copy())
    monkeypatch.setattr(
        "config.write_changes",
        lambda data: written.update(data)
    )

    result = change_setting("currency", "USD")

    assert result is True
    assert written["currency"] == "USD"


def test_change_setting_valid_datafile(monkeypatch):
    # Camino: parámetro datafile con nombre CSV válido.
    setting = {
        "currency": "Reals",
        "datafile": "expense.csv",
    }

    written = {}

    monkeypatch.setattr("config.configure", lambda: setting.copy())
    monkeypatch.setattr("config.check_file_name", lambda value: True)
    monkeypatch.setattr(
        "config.write_changes",
        lambda data: written.update(data)
    )

    result = change_setting("datafile", "gastos.csv")

    assert result is True
    assert written["datafile"] == "gastos.csv"


def test_change_setting_invalid_datafile(monkeypatch):
    # Camino: parámetro datafile con nombre inválido.
    setting = {
        "currency": "Reals",
        "datafile": "expense.csv",
    }

    monkeypatch.setattr("config.configure", lambda: setting.copy())
    monkeypatch.setattr("config.check_file_name", lambda value: False)

    result = change_setting("datafile", "gastos.txt")

    assert result is False


def test_change_setting_invalid_parameter(monkeypatch):
    # Camino: parámetro diferente de currency y datafile.
    setting = {
        "currency": "Reals",
        "datafile": "expense.csv",
    }

    monkeypatch.setattr("config.configure", lambda: setting.copy())

    result = change_setting("invalid", "value")

    assert result is False

# ==========================================
# Tests de la función check_file_name()
# ==========================================

def test_check_file_name_valid_csv():
    # Camino donde el nombre del archivo termina en .csv.
    assert check_file_name("gastos.csv") is True


def test_check_file_name_invalid_extension():
    # Camino donde el archivo tiene una extensión diferente.
    assert check_file_name("gastos.txt") is False

# ==========================================
# Test de la función write_changes()
# ==========================================

def test_write_changes(tmp_path, monkeypatch):
    # Este test pertenece a la función write_changes().
    # Verifica que los cambios sean escritos correctamente
    # en el archivo setting.json.
    monkeypatch.chdir(tmp_path)

    data = {
        "currency": "USD",
        "datafile": "gastos.csv",
    }

    write_changes(data)

    setting_file = tmp_path / "setting.json"

    assert setting_file.exists()

    content = setting_file.read_text(encoding="utf-8")

    assert '"currency": "USD"' in content
    assert '"datafile": "gastos.csv"' in content