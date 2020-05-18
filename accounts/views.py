from django.shortcuts import render


def sign_up(request):
    data = {'title': 'Регистрация'}
    return render(request, 'accounts/sign_up.html', context=data)


def sign_in(request):
    data = {'title': 'Вход'}
    return render(request, 'accounts/sign_in.html', context=data)


def sign_out(request):
    data = {'title': 'Выход из системы'}
    return render(request, 'accounts/sign_up.html', context=data)
