# Project Title

Название проекта: Enterprise Customer Relationship Management (eCRM) Backend

# Description

Проект eCRM Backend представляет собой RESTful API, разработанную с использованием Flask и SQLalchemy. Она предоставляет интерфейс для управления клиентами, заказами, продуктами и другими аспектами бизнес-процессов в компании.

# Stack

- Flask: Микрофреймворк для Python, который позволяет создавать веб-приложения.
- SQLalchemy: ORM (Object-Relational Mapping) для Python, который позволяет работать с базами данных через Python объекты.

# Routes

## Регистрация

- **URL**: `/api/v0.1/register`
- **Метод**: `POST`
- **Описание**: Регистрирует нового пользователя в системе.
- **Параметры**:
  - `username`: Имя пользователя.
  - `password`: Пароль пользователя.
- **Пример запроса**:
  ```json
  {
    "username": "user123",
    "password": "password123"
  }
  ```
- **Пример ответа**:
  ```json
  {
    "message": "The user has been successfully created"
  }
  ```
  - `201`: Пользователь успешно создан.
  - `400`: Имя пользователя и пароль обязательны для заполнения.

## Вход

- **URL**: `/api/v0.1/login`
- **Метод**: `POST`
- **Описание**: Авторизует пользователя и возвращает токен доступа.
- **Параметры**:
  - `username`: Имя пользователя.
  - `password`: Пароль пользователя.
- **Пример запроса**:
  ```json
  {
    "username": "user123",
    "password": "password123"
  }
  ```
- **Пример ответа**:
  ```json
  {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MX0.sB5fSwVBxCf0_vGS4OSI7Ut9izIpD5Z5AxZd8d0sVzU"
  }
  ```
  - `200`: Успешный вход, возвращает токен доступа.
  - `401`: Неверное имя пользователя или пароль.

## Информация о пользователе

- **URL**: `/api/v0.1/user/info`
- **Метод**: `POST`
- **Описание**: Возвращает информацию о пользователе.
- **Параметры**:
  - `Authorization`: Токен доступа, полученный при входе.
- **Пример запроса**:
  ```json
  {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MX0.sB5fSwVBxCf0_vGS4OSI7Ut9izIpD5Z5AxZd8d0sVzU"
  }
  ```
- **Пример ответа**:
  ```json
  {
    "id": 1,
    "username": "user123",
    "role": "admin",
    "created_at": "2022-01-01T00:00:00Z"
  }
  ```
  - `200`: Возвращает информацию о пользователе.
  - `401`: Неверный токен доступа.