# Sprint_5

Автотесты для сервиса [Stellar Burgers](https://stellarburgers.education-services.ru/) на Python с использованием Selenium и pytest.

## Структура проекта

- `tests/` — тесты, по одному файлу на функциональность:
  - `test_registration.py` — регистрация
  - `test_login.py` — вход
  - `test_personal_account.py` — личный кабинет, переход в конструктор, выход
  - `test_logout.py` — выход из аккаунта
  - `test_constructor.py` — разделы конструктора
- `conftest.py` — фикстуры
- `locators.py` — локаторы элементов
- `helpers.py` — генераторы email и пароля, вспомогательные функции
- `data.py` — адреса страниц и тестовые данные
- `requirements.txt` — зависимости

## Установка

1. Создать виртуальное окружение: `python -m venv .venv`
2. Активировать его
3. Установить зависимости: `pip install -r requirements.txt`

Для запуска нужен Google Chrome.

## Запуск тестов

`pytest -v`
