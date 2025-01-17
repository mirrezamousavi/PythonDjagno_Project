# PythonDjagno_Project
This is educational project for learning python Django. we want to implement two parts of real online Shop that contains products with their categories
#First, we create a database in MSSQL Server, then define the model and migrate it. The steps for creating the project and installing the packages are as follows:

python -m venv shopenv
shopenv\Scripts\activate
pip install django
pip install mssql-django
django-admin startproject shopadmin .
python manage.py startapp shop_UI
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser // For Creating User 
python manage.py runserver       

pip list // To know what packages are installed
