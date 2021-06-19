## Запуск тестов pytest
```bash
python -m pytest .
```
## Запуск с профилировщиком
```bash
python -m cProfile -o program.prof main.py
snakeviz program.prof
```