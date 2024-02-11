# pytest_ui_api

## Шаблон для автоматизации на python

### Шаги
1. Склонировать проект 'git clone git@github.com:Valentina-86/pytest_ui_api.git'
2. Установить все зависимости 'pip install -r requirements.txt'
3. Запустить тесты 'python -m pytest'
4. Сгенерировать отчет 'allure generate allure-files -o allure-report'
5. Открыть отчет 'allure open allure-report'

### Стек:
- selenium
- requests
- pytest
- allure
- configparser
- json

## Структура:
- ./test - тесты
- ./pages - описание страниц
- ./api - хэлперы для работы с API
- ./configuration - провайдер настроек
  - test_config.ini - настройки для тестов
- ./testdata - провайдер тестовых данных
  - test_data.json

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор фала .gitignore](https://www.toptal.com/developers/gitignore)
- [Про configparser](https://docs.python.org/3/library/configparser.html#module-configparser)
- [Про pip freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/)

### Библиотеки
- pip install pytest
- pip install selenium
- pip install requests
- pip install allure
- pip install webdriver-manager