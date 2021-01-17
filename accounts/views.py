from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.http import JsonResponse
from webnotes.models import Webnote, Tool, Pattern, Yarn


def sign_up(request):
    data = dict()
    if request.method == 'GET':
        data['title'] = 'Регистрация'
        return render(request, 'accounts/sign_up.html', context=data)
    elif request.method == 'POST':
        log_in = request.POST.get('login')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        email = request.POST.get('email')

        # Каскад проверок данных (валидация):
        if pass1 != pass2:
            data['title'] = 'Отчет о регистрации'
            data['color_mess'] = 'red'
            data['report_mess'] = 'Пароли не совпадают!'
        elif pass1 == '':
            # Остальные проверки:
            pass
        else:
            # Техническая проверка:
            data['login'] = log_in
            data['pass1'] = pass1
            data['pass2'] = pass2
            data['email'] = email

            # Добавление пользователя в БД
            user = User.objects.create_user(log_in, email, pass1)
            user.save()

            # Отчет о регистрации
            data['title'] = 'Отчет о регистрации'
            if user is None:
                data['color_mess'] = 'red'
                data['report_mess'] = 'В регистрации отказанно!'
            else:
                data['color_mess'] = 'green'
                data['report_mess'] = 'Регистрация успешно завершена!'

        return render(request, 'accounts/reports.html', context=data)


def sign_in(request):
    data = dict()
    if request.method == 'GET':
        data['title'] = 'Вход'
        return render(request, 'accounts/sign_in.html', context=data)
    elif request.method == 'POST':
        log_in = request.POST.get('login')
        pass1 = request.POST.get('pass1')

        # Проверка подлиности
        user = authenticate(request, username=log_in, password=pass1)
        if user is None:
            data['title'] = 'Отчет об авторизации'
            data['color_mess'] = 'red'
            data['report_mess'] = 'Пользователь не найден!'
            return render(request, 'accounts/reports.html', context=data)
        else:
            login(request, user)
            return redirect('/home')


def sign_out(request):
    logout(request)
    return redirect('/home')


def profile(request):
    data = dict()
    data['title'] = 'Профиль'
    data['number_webnotes'] = Webnote.objects.filter(user_id=request.user.id).count()
    data['number_patterns'] = Pattern.objects.filter(user_id=request.user.id).count()
    data['number_tools'] = Tool.objects.filter(user_id=request.user.id).count()
    data['number_yarns'] = Yarn.objects.filter(user_id=request.user.id).count()
    return render(request, 'accounts/profile.html', context=data)


def ajax_reg(request):
    response = dict()
    login_y = request.GET.get('login')

    try:
        User.objects.get(username=login_y)
        response['message'] = 'Логин занят'
    except User.DoesNotExist:
        response['message'] = 'Логин свободен'
    return JsonResponse(response)


# def pass_change(request):
#     data = dict()
#     if request.method == 'GET':
#         if request.user.is_authenticated:
#             data['title'] = 'Форма для смены пароля'
#             return render(request, 'accounts/password_change_form.html', context=data)
#         else:
#             logout(request)
#             return redirect('sign_in/')
#     elif request.method == 'POST':
#         old_pass = request.POST.get('old_pass')
#         new_pass1 = request.POST.get('new_pass1')
#         new_pass2 = request.POST.get('new_pass2')
#         # Смена пароля пользователя
#
#         return render(request, 'accounts/password_change_form.html', context=data)
#
#
# def pass_change_done(request):
#     data = dict()
#     data['title'] = 'Пароль изменен'
#     return render(request, 'accounts/password_change_done.html', context=data)
