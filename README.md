python -m venv venv

source venv/Scripts/activate

pip install django

django-admin --help

django-admin startproject empresas

cd empresas
python manage.py --help

python manage.py runserver

python manage.py startapp proveedores_app

