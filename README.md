# Консольное приложение для управления библиотекой книг

## Описание проекта
Это консольное приложение предоставляет функционал для управления библиотекой книг. Пользователь может добавлять книги, удалять книги, просматривать список книг, осуществлять поиск книг, а также изменять статус наличия книг в библиотеке. Приложение использует JSON-файл для долгосрочного хранения информации о книгах.

---

## Основные функции

### 1. Добавление книги
Пользователь может добавить новую книгу в библиотеку с указанием:
- Названия
- Автора
- Года издания

Каждой книге автоматически присваивается уникальный `id`.

---

### 2. Удаление книги
Позволяет удалить книгу по её `id`. Перед удалением программа подтверждает действие у пользователя. При попытке удалить книгу по несуществующему `id` пользователю будет выведено соответствующее уведомление.

---

### 3. Список книг
Программа предоставляет функцию вывода списка всех книг в табличной форме. Для каждой книги отображаются:
- id
- Автор
- Название
- Год издания
- Статус (в наличии или выдана)

---

### 4. Поиск кнги
Пользователь может осуществлять поиск книг по следующим критериям:
- Название
- Автор
- Год издания

Данные о найденных книгах выводятся в табличной форме. В случае отсутствия кнги по запросу, пользователю выводится соответствующее уведомление.

---

### 5. Изменение статуса книги
Позволяет изменить статус книги по её `id`. Перед изменением статуса программа подтверждает действие у пользователя. При попытке изменить статус книги по несуществующему `id` пользователю будет выведено соответствующее уведомление.

---

### 6. Сохранение/загрузка данных
Все данные о книгах автоматически сохраняются в файл `db.json`, а также могут быть загружены из него при запуске приложения. Это позволяет продолжить работу с библиотекой после перезапуска программы.

---

## Зависимости
Для работы приложения необходим Python версии 3.8 и выше. Используются встроенные библиотеки:
- `json` (для работы с данными)
- `time` (для создания пауз и улучшения пользовательского опыта)

---

## Установка

1. Скачайте репозиторий или файл `main.py`.
2. Убедитесь, что установлен Python 3.8+.
3. Запустите приложение командой:
   ```bash
   python main.py
   ```

---

## Использование

### Основное меню

После запуска пользователю будет предложено основное меню с доступными командами:

- Добавить новую книгу
- Удалить книгу
- Просмотреть список книг
- Запустить поиск книг
- Изменить статус наличия книги

---

## Структура данных

Каждая книга в библиотеке хранится в виде словаря следующего формата:

```json
{
    "id": {
        "title": "Название книги",
        "author": "Автор книги",
        "year": "2024",
        "status": true
        }
}
```

id: Уникальный идентификатор книги
title: Название книги
author: Автор книги
year: Год издания
status: Статус книги (True — в наличии, False — выдана)
