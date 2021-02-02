# the-insta

## v1.0 Demo

![todo_demo](/assets/todo_demo.gif)

# venv 
1. Create venv name with mysite
   - `python3 -m venv theinsta`
1. `cd insta/bin` or `cd insta/Script`
1. `. activate`

## Install prerequisites

1. python -m pip install --upgrade pip
1. pip install psycopg2
1. pip install djangorestframework django-cors-headers
1. pip install django-rest-swagger

## Create postgreSQL database in instance

1. `CREATE DATABASE theinsta;`
1. `GRANT ALL PRIVILEGES ON DATABASE theinsta To user_id;`
1. Make `dev_settings.py` in root directory
    ```python
    # /dev_settings.py
    SECRET_KEY = '*************************'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': '*********',
            'USER': '*********',
            'PASSWORD': '*******',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
    ```

## Launch Project in instance console

1. Activate venv
1. `cd projects/mysite`
1. `python manage.py migrate`
1. Make sure the static IP address is set as [here][2]
1. `python manage.py runserver 0:8000`

# Dev Environment

- window 10 (Ubuntu20.04 also possible)
- python 3.6.8
- django 3.1.5

# Reference


[1]: https://wikidocs.net/75559
[2]: https://github.com/hwanseok-dev/The-PyBo/blob/master/config/settings.py#L24

