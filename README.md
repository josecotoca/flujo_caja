## Crear entorno
```
python -m venv venv
```

## Activar entorno
```
source venv/Scripts/activate
```

## Crear proyecto y apps
```
pip install django

django-admin --help

django-admin startproject nombre .

python manage.py startapp proveedores_app
```

## Correr proyecto
```
python manage.py runserver
```

python manage.py makemigrations
python manage.py migrate