# django_cart
Instructions to create the project from scratch:

python -m venv myenvironment  
cd myenvironment  
Scripts\activate  
//deactivate   
pip install django  
//in you have problems on win10 with sll install:  
//https://slproweb.com/products/Win32OpenSSL.html  
//to check django version:  
python  
import django  
django.get_version()  
django.VERSION  
//while inside of myenvironment with it activated:  
django-admin startproject perfectcushion   
django_cart\myenvironment\perfectcushion>python manage.py migrate  
python manage.py runserver  
python manage.py startapp shop  
//edit shop/views.py  
//edit perfectcushion/urls.py  
//add shop to settings.py  
python manage.py runserver  