# Ресторанное Меню API

## Обзор
API для управления категориями блюд и едой в ресторане с многоязычной поддержкой.

## Модели
- `FoodCategory`: Категории блюд
- `Food`: Блюда с расширенными атрибутами

## Эндпоинты
- `GET /api/v1/foods/`: Получение списка категорий с опубликованными блюдами

## Технологии
- Django
- Django Rest Framework
- PostgreSQL

## Установка
```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
