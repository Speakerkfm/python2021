import main
import pandas as pd


def test_prepare_train_set_ok_4_2_30():
    expected = pd.read_csv('test_expected/expected_1.csv')
    result = main.prepare_train_set(logs_path='test/user01.csv',
                                    session_length=4,
                                    window_size=2,
                                    max_duration=30 * 60)
    assert result.compare(expected).empty


def test_prepare_train_set_ok_10_2_30():
    expected = pd.read_csv('test_expected/expected_2.csv')
    result = main.prepare_train_set(logs_path='test/user01.csv',
                                    session_length=10,
                                    window_size=2,
                                    max_duration=30 * 60)
    assert result.compare(expected).empty


def test_prepare_train_set_ok_4_2_4():
    expected = pd.read_csv('test_expected/expected_3.csv')
    result = main.prepare_train_set(logs_path='test/user01.csv',
                                    session_length=4,
                                    window_size=2,
                                    max_duration=4 * 60)
    assert result.compare(expected).empty


def test_prepare_train_set_ok_4_2_5_two_users():
    expected = pd.read_csv('test_expected/expected_4.csv')
    result = main.prepare_train_set(logs_path='test/*.csv',
                                    session_length=4,
                                    window_size=2,
                                    max_duration=5 * 60)
    assert result.compare(expected).empty
