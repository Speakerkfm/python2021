Запуск тестов unittest

```
python -m unittest -v one_hot_encoder_test.py
```

Результат выполнения

```
test_empty_args (one_hot_encoder_test.TestEncoder) ... ok
test_ok_four_cities_with_copies (one_hot_encoder_test.TestEncoder) ... ok
test_ok_two_diff_cities (one_hot_encoder_test.TestEncoder) ... ok
test_ok_two_same_cities (one_hot_encoder_test.TestEncoder) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

Запуск тестов pytest

```
python -m pytest pytest_one_hot_encoder_test.py
```

Результат выполнения

```
=========================================================================== test session starts ============================================================================
platform darwin -- Python 3.7.3, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: /Users/usanin/PycharmProjects/python2021/testing/one_hot_encoder
collected 4 items                                                                                                                                                          

pytest_one_hot_encoder_test.py ....                                                                                                                                  [100%]

============================================================================ 4 passed in 0.01s =============================================================================
```