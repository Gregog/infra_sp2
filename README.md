# Докеризация API для Ya|MDb. Интернет-сервис о кино на базе Django REST

Проект выполнялся в рамках учебного курса Яндекс.Практикум

## Установка

#### Шаг первый. Проверьте установлен ли у вас Docker. 

```Ваш терминал
docker -v
```
Если у вас не отобразилась информация о версии вашего Docker, то установите его. [Официальная инструкция](https://docs.docker.com/engine/install/)

##### Шаг второй. Сборка контейнера.
```Ваш терминал
docker-compose build
```
##### Шаг третий. Запуск контейнера.
```Ваш терминал
docker-compose up
```
##### Шаг четвертый. База данных.
```Ваш терминал
docker-compose run web python manage.py migrate --no-input
```
## Использование
### Создание суперпользователя Django.
```Ваш терминал
docker-compose run web python manage.py createsuperuser
```
### Импорт данных в формате .json.
```Ваш терминал
docker-compose run web python manage.py loaddata path/to/your/json
```
В папке fixtures вы найдете пример такого файла.
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
[Docker cheatsheet](http://dockerlabs.collabnix.com/docker/cheatsheet/)
[Django loaddata документация](https://docs.djangoproject.com/en/3.0/ref/django-admin/#django-admin-dumpdata)
[README API_YaMDb](https://github.com/Gregog/api_yamdb/blob/master/README.md)

## Почта для обратной связи idzaoshang@gmail.com
