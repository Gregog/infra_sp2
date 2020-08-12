# Докеризация API для Ya|MDb. Интернет-сервис о кино на базе Django REST

Проект выполнялся в рамках учебного курса Яндекс.Практикум

## Установка

#### Шаг первый. Проверьте установлен ли у вас Docker

```Ваш терминал
docker -v
```
Если у вас все еще не установлен Docker и вы используете Linux, то воспользуйтесь скриптом:
```Ваш терминал
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh # эта команда запустит его
<<<<<<< HEAD
```
Если же у вас другая ОС, то воспользуйтесь [Официальная инструкцией](https://docs.docker.com/engine/install/).

##### Шаг второй. Сборка контейнера
```Ваш терминал
docker-compose build
```
##### Шаг третий. Запуск контейнера
```Ваш терминал
docker-compose up
```
##### Шаг четвертый. База данных
```Ваш терминал
docker-compose run web python manage.py migrate --no-input
```
## Использование
### Создание суперпользователя Django
```Ваш терминал
docker-compose run web python manage.py createsuperuser
```
### Импорт данных в формате .json
```Ваш терминал
docker-compose run web python manage.py loaddata path/to/your/json
```
Пример инициализации стартовых данных:
```Ваш терминал
docker-compose run web python manage.py loaddata fixtures/fixture.json
```
### Выключение контейнера
```Ваш терминал
docker-compose down
```
### Удаление всех Docker контейнеров
```Ваш терминал
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```

### Полезные ссылки
[Docker cheatsheet](http://dockerlabs.collabnix.com/docker/cheatsheet/) <br>

[Django loaddata документация](https://docs.djangoproject.com/en/3.0/ref/django-admin/#django-admin-dumpdata) <br>

[README API_YaMDb](https://github.com/Gregog/api_yamdb/blob/master/README.md) <br>

## Почта для обратной связи idzaoshang@gmail.com
