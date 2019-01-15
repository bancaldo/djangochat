# Django-channels chat

This is a Django application example only.
This app uses channels to simulate a chat over websockets.
It uses Redis as server.

## Install

Create a virtual environment and install the following packages:

```
pip install django
```

Install twisted by wheel package from https://www.lfd.uci.edu/~gohlke/pythonlibs/

```
pip install venv\Twisted-18.9.0-cp37-cp37m-win32.whl
```
and then

```
pip install channels channels_redis pywin32
```

## Run server

Run Redis-server and django server:

```
python manage.py runserver
```

finally go to http://127.0.0.1:8000/chat

## Licence

GPL
