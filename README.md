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
//to add products from a csv file, this option must be enabled, do the following:
pip install django-import-export
//in settings.py add the following:
//1.)'import_export' to Installed apps  
//2.) IMPORT_EXPORT_USE_TRANSACTIONS = True 
//in admin.py: from import_export.admin import ImportExportModelAdmin  
//adjust the ProductAdmin argument to have ImportExportModelAdmin   
//now you can run the server  
//to add thumbnail images to the product listing in the admin page:  
from django.utils.html import format_html   
//in admin.py create a function def thumbnail(self,obj): and have it return a string with an img tag  
//in the terminal, retrieve the data with:  
python manage.py shell  
from shop.models import Category, Product  
Product.objects.all()  
p= Product.objects.all()  
c= Category.objects.all()  
//Product.objects.get(id=1)  
//Product.objects.get(pk=1)  
//catId1 = Category.objects.get(id=1)  
//prodWCatId1 = Product.objects.filter(category=catId1)  
//prodEle = Product.objects.filter(name__startswith='Elephant')  
//prodEleCont = Product.objects.filter(name__contains='Elephant')  
//Product.objects.filter(price__range(10,25))  
//p=Product.objects.create(name='pug dog', price=30)   
//p.save()  
//p.delete()  

