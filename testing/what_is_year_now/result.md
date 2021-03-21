Запуск тестов pytest

```
python -m pytest --cov .
```

Результат выполнения

```
=========================================================================== test session starts ============================================================================
platform darwin -- Python 3.7.3, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: /Users/usanin/PycharmProjects/python2021/testing/what_is_year_now
plugins: cov-2.11.1
collected 3 items                                                                                                                                                          

what_is_year_now_test.py ...                                                                                                                                         [100%]

---------- coverage: platform darwin, python 3.7.3-final-0 -----------
Name                       Stmts   Miss  Cover
----------------------------------------------
what_is_year_now.py           19      0   100%
what_is_year_now_test.py      28      0   100%
----------------------------------------------
TOTAL                         47      0   100%


============================================================================ 3 passed in 0.24s =============================================================================
```