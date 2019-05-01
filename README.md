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
//edit shop/models.py  
//edit perfectcushion/settings.py with MEDIA_ROOT  
//edit perfectcushion/urls.py with: if settings.DEBUG:  
//with environment enabled run the following:  
\myenvironment\perfectcushion>pip install Pillow  
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
//ckd16 ckd1618@gmail.com password123
//now you can go to localhost:8000/admin since you created the superuser
python manage.py runserver
//edit shop/admin.py
python manage.py runserver
//now you can create products and categories from the admin page, while uploading images and descriptions