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

//in shop create create folder templates, then in templates create shop folder  
//in perfectcushion/settings.py add to TEMPLATES list the following: 'DIRS': [os.path.join(BASE_DIR, 'shop','templates/')],  
//in shop/templates/shop create base.html
//create a folder called img inside of static and add a logo and banner images
//in shop/templates create footer.html header.html navbar.html
//in views add the function allProdCat  
//create a file in perfectcushion/shop called urls.py
//goto pein django.urls import include and then add a reference to shop/urls.py under urlpatterns  
//create a file in shop/templates/shop called category.html  

//**********admin and 3 webpages are up****************

//in perfectcushion/shop create context_processors.py
//add it to templates in settings.py

//localize bootstrap after copy pasting the code into static under css and js folders, run:
python manage.py collectstatic
//with this command line I collect all the static data along with the bootstrap js and css files

//fonts.google.com
//select roboto and copy paste the link
//in the custom.css file, paste the rule under body {}

//when dealing with css div.myclass refers to a class found on the same line
// div .myclass refer to two separate lines

//acquire fontawesome 5.0.13 and add its webfont folder to static and its all.min.css file to static/css
python manage.py collectstatic

python manage.py startapp search_app
//create the templates folder in search_app and add it to installed apps in settins.py, besure to add it to templates = 'DIRS' as well

python manage.py startapp cart

python manage.py makemigrations
python manage.py migrate
// whenever you create a templates folder, make sure you register the folder in settings.py under Templates

pip install stripe
//add stripe to installed apps in settings.py

python manage.py startapp order
//add order to settings.py

//copy C:\Users\ckd16\Desktop\ag\django_cart\myenvironment\Lib\site-packages\django\contrib\admin\templates\admin\edit_inline\tabular.html
//this file controls the behavior of the order item section of the order record

pip install django-crispy-forms
//to help design the signup form, via the aid of bootstrap classes
//after installing, make sure to register it in settings.py
// also add: CRISPY_TEMPLATE_PACK = 'bootstrap4'