from .sqlite_db import SqliteDatabase
from unittest.mock import patch, MagicMock


@patch('sqlite3.connect')
def test_create_tables_ok(mock_connect):
    cm = MagicMock()
    mock_connect.return_value = cm

    int_field = MagicMock()
    int_field.to_sql.return_value = 'test_field_int INTEGER'

    char_field = MagicMock()
    char_field.to_sql.return_value = 'test_field_char TEXT'

    class TestEntity:
        _name = 'test_entity'
        _data = {
            'test_field_int': {'_meta': int_field},
            'test_field_char': {'_meta': char_field},
        }

    db = SqliteDatabase('test.db')

    db.connect()
    db.create_tables([TestEntity])
    db.close()

    cm.execute.assert_called_once()
    cm.execute.assert_called_with(
        'create table if not exists test_entity ('
        'test_field_int INTEGER, '
        'test_field_char TEXT);')
    cm.close.assert_called_once()


@patch('sqlite3.connect')
def test_save_entity_ok(mock_connect):
    cm = MagicMock()
    mock_connect.return_value = cm

    int_field = MagicMock()
    int_field.to_sql.return_value = 'test_field_int INTEGER'

    char_field = MagicMock()
    char_field.to_sql.return_value = 'test_field_char TEXT'

    class TestEntity:
        _name = 'test_entity'
        _data = {
            'test_field_int': {'_meta': int_field},
            'test_field_char': {'_meta': char_field},
        }

    db = SqliteDatabase('test.db')

    db.connect()
    my_entity = TestEntity()
    my_entity._data['test_field_int']['_value'] = 123
    my_entity._data['test_field_char']['_value'] = 'test_value'
    db.save_entity(my_entity)
    db.close()

    cm.execute.assert_called_once()
    cm.execute.assert_called_with(
        'replace into test_entity('
        'test_field_int, test_field_char) '
        'values(123, \'test_value\');')
    cm.close.assert_called_once()


@patch('sqlite3.connect')
def test_select_entities_ok(mock_connect):
    cm = MagicMock()
    cm.execute.return_value = [[12345, 'test_value']]
    mock_connect.return_value = cm

    int_field = MagicMock()
    int_field.to_sql.return_value = 'test_field_int INTEGER'

    char_field = MagicMock()
    char_field.to_sql.return_value = 'test_field_char TEXT'

    class TestEntity:
        _name = 'test_entity'
        _data = {
            'test_field_int': {'_meta': int_field},
            'test_field_char': {'_meta': char_field},
        }

    db = SqliteDatabase('test.db')

    db.connect()
    res = db.select_entities(TestEntity)
    db.close()

    assert len(res) == 1
    assert res[0].test_field_int == 12345
    assert res[0].test_field_char == 'test_value'

    cm.execute.assert_called_once()
    cm.execute.assert_called_with(
        'select test_field_int, test_field_char from test_entity;')
    cm.close.assert_called_once()
