from django.shortcuts import render
from . import models

#Список всех продуктов
def all_products(request):
    if request.method == "GET":
        query  = models.Product.objects.all().order_by('-id')
        context_object_name = {
            'all_products': query,
        }
        return render(request, template_name='products_home/all_products.html',
                      context=context_object_name)

#для Детская
def children_products(request):
    if request.method == "GET":
        query  = models.Product.objects.filter(tags__name='для Детская').order_by('-id')
        context_object_name = {
            'children': query,
        }
        return render(request, template_name='products_home/children.html',
                      context=context_object_name)

#для Подростковая
def teenage_products(request):
    if request.method == "GET":
        query  = models.Product.objects.filter(tags__name='для Подростковая').order_by('-id')
        context_object_name = {
            'teenage': query,
        }
        return render(request, template_name='products_home/teenage.html',
                      context=context_object_name)