# Product Store API

## Описание

Product Store API — это REST API для управления продуктами интернет-магазина, реализованное на Django и Django REST Framework. API позволяет выполнять CRUD операции с товарами, категориями и ценами, а также поддерживает управление остатками на складе. 

## 🚀 Функциональные возможности

- CRUD операции для управления товарами, типами товаров и ценами
- Административная панель с расширенными возможностями поиска и фильтрации
- API для уменьшения остатка товаров на складе
- Поддержка различных валют

## 📋 Технологический стек

- **Python** 3.11+
- **Django** 5.1+
- **Django REST Framework** 3.14+

## 🛠 Установка и настройка

### 1. Клонирование репозитория

```bash
git clone https://github.com/Lisnevskiy/ProductStore.git
```

### 2. Установка зависимостей

Убедитесь, что у вас установлен [Pipenv](https://pipenv.pypa.io/en/latest/). Установите зависимости:

```bash
pipenv install
```

### 3. Настройка переменных окружения

Создайте файл `.env` в корневой директории и добавьте необходимые переменные окружения, примеры которых, указаны в файле .env.sample

### 4. Применение миграций

Примените миграции базы данных:

```bash
python manage.py migrate
```

### 5. Создание суперпользователя

Для доступа к админ-панели создайте суперпользователя:

```bash
python manage.py createsuperuser
```

### 6. Запуск сервера

Запустите сервер разработки:

```bash
python manage.py runserver
```

Приложение будет доступно по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Использование API

API включает следующие основные эндпоинты:

- `GET /api/products/` - Получить список всех продуктов.
- `POST /api/products/` - Создать новый продукт.
- `GET /api/products/{id}/` - Получить информацию о продукте.
- `PUT /api/products/{id}/` - Обновить продукт.
- `DELETE /api/products/{id}/` - Удалить продукт.
- `POST /api/products/{id}/reduce-stock/` - Уменьшить остаток продукта на складе.

### Пример запроса

Пример POST-запроса для создания нового продукта:

```http
POST /api/products/
Content-Type: application/json

{
    "name": "VR Headset",
    "quantity": 20,
    "barcode": "6655443322110",
    "type": {
        "name": "Gaming Accessories",
        "description": "Accessories for immersive gaming"
    },
    "price": {
        "currency": "JPY",
        "amount": 12500
    }
}
```

## Структура проекта

```plaintext
ProductStore/
├── product/                   # Основное приложение с моделями и представлениями
│   ├── migrations/          # Миграции базы данных
│   ├── models.py            # Модели данных
│   ├── views.py             # Представления и логика API
│   └── serializers.py       # Сериализаторы для обработки данных
├── config/
│   ├── settings.py          # Настройки Django
│   ├── urls.py              # URL маршруты проекта
│   └── wsgi.py              # Точка входа для WSGI сервера
└── manage.py                # Скрипт управления Django
```

## Контакты

Если у вас есть вопросы или предложения, пожалуйста, свяжитесь со мной по адресу [lisnevskiy14@gmail.com](mailto:lisnevskiy14@gmail.com).