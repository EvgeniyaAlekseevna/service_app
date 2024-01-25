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



# Тестирование
