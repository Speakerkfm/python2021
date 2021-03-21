Запуск тестов с использованием doctest

```
python -m doctest -o NORMALIZE_WHITESPACE -v morse.py
```

Результат запуска скрипта

```
Trying:
encode('SOS')
Expecting:
'... --- ...'
ok
Trying:
encode('a')
Expecting:
Traceback (most recent call last):
...
KeyError: 'a'
ok
Trying:
encode('YES') # doctest: +ELLIPSIS
Expecting:
'-.--...'
ok
2 items had no tests:
morse
morse.decode
1 items passed all tests:
3 tests in morse.encode
3 tests in 3 items.
3 passed and 0 failed.
Test passed.
```

Запуск параметризованных тестов
```
pytest morse_test.py
```

Результат выполнения
```
=========================================================================== test session starts ============================================================================
platform darwin -- Python 3.7.3, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: /Users/usanin/PycharmProjects/python2021/testing/morse
collected 1 item                                                                                                                                                           

morse_test.py .                                                                                                                                                      [100%]

============================================================================ 1 passed in 0.02s =============================================================================
```
