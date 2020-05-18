from django.shortcuts import render


def index(request):
    data = {'title': 'Главная'}
    return render(request, 'home/index.html', context=data)


def about(request):
    data = {'title': 'О сайте'}
    return render(request, 'home/about.html', context=data)


def contacts(request):
    data = {'title': 'Контакты'}
    return render(request, 'home/contacts.html', context=data)
