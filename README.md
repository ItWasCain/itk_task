### Общее описание проекта:
Проект представляет web службу на основе REST архитектуры.
Данные передаются в формате JSON.

API имеет два эндпоинта:

```
POST:
    api/v1/wallets/{WALLET_UUID}/operation
GET:
    api/v1/wallets/{WALLET_UUID}
```

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/ItWasCain/itk_task.git
```

```
cd itk_task/test_project/infra/
docker compose up
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py collectstatic
docker compose exec backend python manage.py createsuperuser

```



### Примеры api запросов:

Получение информации о кошельке:

запрос:
```
get http://localhost:8000/api/v1/wallets/{WALLET_UUID}/
```
ответ:
```
{
    "wallet_uuid": "eyJ0eXAi",
    "amount": 0
}
```

Проведение операции зачисления:

запрос:
```
post http://localhost:8000/api/v1/wallets/{WALLET_UUID}/operation
{
    "operation_type": "DEPOSIT",
    "amount": 100
}
```
ответ:
```
{
    "wallet_uuid": "eyJ0eXAi",
    "amount": 100
}
```

Проведение операции списания:

запрос:
```
post http://localhost:8000/api/v1/wallets/{WALLET_UUID}/operation
{
    "operation_type": "WITHDRAW",
    "amount": 100
}
```
ответ:
```
{
    "wallet_uuid": "eyJ0eXAi",
    "amount": 0
}
```


### Использованные технологии:

    Python, Django, Django Rest Framework, PostgeSQL, Docker.


### Разработчик:
Никита Песчанов https://github.com/ItWasCain

