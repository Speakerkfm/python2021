## Запуск тестов pytest
```bash
python -m pytest .
```
## Запуск с профилировщиком
```bash
python -m cProfile -o program.prof bonus_calculator.py
snakeviz program.prof
```