from django.shortcuts import render
from webnotes.models import Webnote, Pattern


def index(request):
    data = dict()
    data['title'] = 'Главная'
    data['public_webnotes'] = Webnote.objects.filter(access=2)       # [:10]
    data['public_patterns'] = Pattern.objects.filter(webnote__access=2)
    return render(request, 'home/index.html', context=data)


def about(request):
    data = {'title': 'О сайте'}
    return render(request, 'home/about.html', context=data)


def contacts(request):
    data = {'title': 'Контакты'}
    return render(request, 'home/contacts.html', context=data)
