# Учебный проект Оптимизация Django от Senior Pomidor Developer

# Зависимости
Для настройки приложения скопируйте `.env.sample` в файл `.env`:
```shell
cp .env.sample .env
```

# Требования
# Запуск

docker-compose build
docker-compose up
docker-compose run web-app
docker-compose run --rm  web-app sh -c "django-admin startproject service ."

запуск
docker-compose build
docker-compose up

создание миграций 
docker-compose run --rm  web-app sh -c "python manage.py migrate"

создание админа
docker-compose run --rm  web-app sh -c "python manage.py createsuperuser"

создание приложения/проекта
docker-compose run --rm  web-app sh -c "python manage.py startapp clients"
docker-compose run --rm  web-app sh -c "python manage.py startapp services"

регистрирум приложения в settings

docker-compose run --rm  web-app sh -c "python manage.py makemigrations clients"
docker-compose run --rm  web-app sh -c "python manage.py migrate clients"

docker-compose run --rm  web-app sh -c "python manage.py makemigrations services"
docker-compose run --rm  web-app sh -c "python manage.py migrate services"

http://127.0.0.1:8000/api/subscription/?format=json

docker-compose run --rm  web-app sh -c "python manage.py shell"


flower
http://127.0.0.1:5555/

# Тестирование
