# Places-Remember
веб-приложение, с помощью которого люди смогут хранить свои впечатления о посещенных местах
Приложение написано на python версии 3.10
# Запуск проекта
Запуск проекта можно осуществить на локальном компьютере, либо через docker
# Запуск через Docker
Сборка проекта: ```docker-compose build```  
Миграция моделей: docker-compose ```docker-compose run --rm django_app python manage.py migrate```  
Примечание. Может возникнуть ошибка, что django не может подключиться к базе данных. Для устранения ошибки повторно выполните
вышеуказанную команду  
Запуск web приложения: ```docker-compose up```
После запуска контейнеров перейдите по следующему URL в своем браузере: http://localhost:80  
Запуск тестов: ```docker-compose run --rm django_app python manage.py test app```

# Запуск на локальном компьютере
* Убедитесь, что у вас на компьютере установлен PostgreSQL (pgAdmin4)
* Создайте виртуальное окружение с python версии 3.10
* Установите необходимые зависимости командой ```pip install -r requirements.txt```
* Создайте в корневой директории файл .env, и поместите туда следующие данные:
  * DB_NAME
  * DB_USER
  * DB_PASSWORD
  * DB_HOST
  * DB_PORT
  * SOCIAL_AUTH_VK_OAUTH2_KEY
  * SOCIAL_AUTH_VK_OAUTH2_SECRET
 Последние два параметры можно получить, создав приложение в [vk id](https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/intro/start-page)

* Перейдите в директорию djangoProject
* Запустите приложение командой ```python manage.py runserver localhost:8000```

Из функциональности не удалось реализовать тесты для получения посещенных мест.
