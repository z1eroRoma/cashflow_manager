# Управление движением денежных средств (ДДС)

Веб-приложение для учета, управления и анализа движения денежных средств.

---

## 📋 Содержание
- [Требования](#-требования)
- [Установка](#-установка)
- [Настройка базы данных](#-настройка-базы-данных)
- [Запуск](#-запуск)
- [Наполнение начальными данными](#-наполнение-начальными-данными)
- [Структура проекта](#-структура-проекта)
- [Лицензия](#-лицензия)

---

## 📌 Требования
- Python 3.12 или выше
- pip (менеджер пакетов Python)

---

## 🛠 Установка

### 1. Клонирование репозитория
```bash
git clone <URL_репозитория>
cd cashflow_manager
```

### 2. Создание виртуального окружения
```bash
python -m venv .venv
```

### 3. Активация виртуального окружения

#### На Windows:
```bash
.venv\Scripts\activate
```

#### На macOS/Linux:
```bash
source .venv/bin/activate
```

### 4. Установка зависимостей
```bash
pip install django==5.2.6
pip install python-dotenv
```

---

## 🗃 Настройка базы данных

### 1. Применение миграций
```bash
python manage.py makemigrations
python manage.py migrate
```

### 2. Создание суперпользователя (опционально)
```bash
python manage.py createsuperuser
```
Следуйте инструкциям для ввода имени пользователя, email и пароля.

---

## 🚀 Запуск

### Запуск веб-сервера для разработки
```bash
python manage.py runserver
```

После успешного запуска сервера, вы сможете открыть проект в браузере по адресу:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Для доступа к админ-панели перейдите по адресу:
[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📦 Напольнение начальными данными (опционально)

### Создание фикстур
1. Создайте начальные данные в админ-панели.
2. Сохраните данные в фикстуры:
```bash
python manage.py dumpdata --indent=4 > cashflow/fixtures/initial_data.json
```

### Загрузка фикстур
```bash
python manage.py loaddata initial_data
```

---

## 📂 Структура проекта
```
cashflow_manager/
├── cashflow/
│   ├── migrations/
│   ├── templates/
│   │   └── cashflow/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── cashflow_manager/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .venv/
├── db.sqlite3
└── manage.py
```

---
