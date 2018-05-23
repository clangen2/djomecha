from django.shortcuts import render
from djomecha_app.models import *
from django.http import HttpResponse



def index(request):
    return render(request, 'index.html')

def items(request):
    items = Item.objects.all()
    return render(request, 'items.html', {"items": items})

def item_view(request, title):
    the_item = Item.objects.filter(slug = title)
    return render(request, 'item.html', {"items" : the_item})

def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
        
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
# Create your views here.
