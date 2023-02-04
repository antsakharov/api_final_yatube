# api_final_yatube 

## Описание проекта: 

•	**Назначение:** 

Финальная версия Api социальной сети yatube

•	**Реализованный функционал:** 

С помощью api_final_yatube можно запрашивать данные о постах, группах, комментариях в социальной сети Yatube, а также создавать новые.

•	**Цель выполнения проекта:**

Получить навыки создания API для собственного проекта

•	**Стек:**

Python 3.7, Django 3.2, DRF, Pillow 8.3.1, Simple JWT

## Инструкция по развёртыванию проекта

•	**Клонируйте репозиторий:**

```csharp 
git clone git@github.com:antsakharov/api_final_yatube.git
```

•	**Установите и активируйте виртуальное окружение:**

**для Linux и MacOS**

```csharp 
python3 -m venv venv
```

**для Windows**

```csharp 
python -m venv venv
```

```csharp 
source venv/bin/activate
```

```csharp 
source venv/Scripts/activate
```

•	**Установите зависимости из файла requirements.txt:**

```csharp 
pip install -r requirements.txt
```

•	**Создайте и выполните миграции:**

```csharp 
python manage.py makemigrations
```

```csharp 
python manage.py migrate
```
## Примеры запросов к API:

Получить список всех постов (GET):
```csharp
http://127.0.0.1:8000/api/v1/posts/
```

Получить определенный пост (GET):
```csharp
http://127.0.0.1:8000/api/v1/posts/1/
```

Получить коментарии определенного поста (GET):
```csharp
http://127.0.0.1:8000/api/v1/posts/1/comments/
```

Получить список всех групп (GET):
```csharp
http://127.0.0.1:8000/api/v1/groups/
```

Создать новый пост (POST):


(Требуется аутентификация)
```csharp
http://127.0.0.1:8000/api/v1/posts/
```

Документация: http://127.0.0.1:8000/redoc/
