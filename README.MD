# Шаблон сайта на Bottle

Минимальный проект: маршруты в `routes.py`, шаблоны в `views/`, статика в `static/`.

## Запуск из консоли

1. Перейти в папку проекта:

   ```bash
   cd /путь/к/MosolovaProject
   ```

2. Создать окружение и поставить зависимости (из корня проекта):

   ```bash
   python3 -m venv .venv
   .venv/bin/python -m pip install -r requirements.txt
   ```

   Windows: `python -m venv .venv` и `.venv\Scripts\python.exe -m pip install -r requirements.txt`

3. Включить окружение в текущей консоли и дальше вызывать команды без пути:

   ```bash
   source .venv/bin/activate
   python app.py
   ```

   Windows: `.venv\Scripts\activate`, затем `python app.py`

   Установка пакетов в том же сеансе: `python -m pip install -r requirements.txt`. Обычно удобнее писать **`python`**, а не `python3`, чтобы использовался интерпретатор из venv.

4. Открыть в браузере: **http://localhost:5555** (порт по умолчанию).

Выход из окружения: `deactivate`.

### Полезные опции

- **Отладка**: `python app.py --debug` или `SERVER_DEBUG=1 python app.py`
- **Хост и порт**: `SERVER_PORT=8080 python app.py` (и при необходимости `SERVER_HOST=0.0.0.0`)
