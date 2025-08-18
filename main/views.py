from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories
# Create your views here.
def index(request):

    categories = Categories.objects.all()
    context= {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
        'categories': categories,
    }
    return render(request, 'main/index.html', context)

def about(request):
    context= {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о нас'
    }
    return render(request, 'main/about.html', context)
def delivery(request):
    context= {
        'title': 'Home - Доставка',
        'content': 'Доставка и оплата',
        'text_on_page': 'Текст о доставке'
    }
    return render(request, 'main/delivery.html', context)
def contact(request):
    context= {
        'title': 'Home - Контакты',
        'content': 'Наши контакты',
        'text_on_page': 'Адреса'
    }
    return render(request, 'main/contacts.html', context)