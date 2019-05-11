from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.http import HttpResponse

def index(request):
  text_var = 'my first django web page'
  return HttpResponse(text_var)

#view for Category

def allProdCat(request, c_slug=None):
  c_page = None
  products = None
  if c_slug != None:
    c_page = get_object_or_404(Category, slug=c_slug)
    products = Product.objects.filter(category=c_page, available=True)
  else:
    products = Product.objects.all().filter(available=True)
  return render(request, 'shop/category.html', {'category':c_page,'products':products})

def ProdCatDetail(request, c_slug, product_slug):
  try:
    product = Product.objects.get(category__slug=c_slug, slug = product_slug) #double underscore after category will utilize the foreign key in the model before checking for slug in category__slug
  except Exception as e:
    raise e
  return render(request, 'shop/product.html', {'product': product})