from django.shortcuts import render, redirect
from webnotes.models import Pattern
from .forms import PatternForm, PatternForm2
from django.contrib.auth import logout
from django.core.paginator import Paginator


def index(request):
    data = dict()
    data['title'] = 'Коллекция узоров'
    all_patterns = Pattern.objects.all()
    data['patterns'] = all_patterns

    paginator = Paginator(all_patterns, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data['page_obj'] = page_obj

    return render(request, 'patterns/index.html', context=data)


def create(request):
    data = dict()
    data['title'] = 'Добавление узора в коллекцию'
    if request.method == 'GET':
        # Блокировка доступа через адресную строку
        # superadmim1 : 777sssL
        if request.user.username == 'superadmim1':
            data['form_pattern'] = PatternForm()
            return render(request, 'patterns/create.html', context=data)
        else:
            # Отправляем на Регистрацию, если не superadmim1
            logout(request)
            return redirect('/accounts/sign_up')
    elif request.method == 'POST':
        filled_form = PatternForm(request.POST, request.FILES)
        filled_form.save()
        # перенаправляем на страничку patterns/index.html, а там запись добовляется в список со всеми записями
        return redirect('/patterns')


def details(request, pattern_id):
    data = dict()
    data['title'] = 'Информация об узоре'
    data['pattern'] = Pattern.objects.get(id=pattern_id)
    return render(request, 'patterns/details.html', context=data)


def edit(request, pattern_id):
    data = dict()
    data['title'] = 'Изменить информацию об узоре'
    pattern = Pattern.objects.get(id=pattern_id)
    if request.method == 'GET':
        if request.user.username == 'superadmim1':
            data['form'] = PatternForm2(instance=pattern)
            data['pattern'] = pattern
            return render(request, 'patterns/edit.html', context=data)
        else:
            logout(request)
            return redirect('/accounts/sign_up')
    elif request.method == 'POST':
        form2 = PatternForm2(request.POST)
        if form2.is_valid():
            pattern.name = form2.cleaned_data['name']
            pattern.image = form2.cleaned_data['image']
            pattern.scheme = form2.cleaned_data['scheme']
            pattern.description = form2.cleaned_data['description']
            pattern.source = form2.cleaned_data['source']
            pattern.save()
        return redirect('/patterns')


def delete(request, pattern_id):
    data = dict()
    data['title'] = 'Удаление узора из коллекции'
    pattern = Pattern.objects.get(id=pattern_id)
    if request.method == 'GET':
        # Блокировка доступа через адресную строку
        if request.user.username == 'superadmim1':
            data['pattern'] = pattern
            return render(request, 'patterns/delete.html', context=data)
        else:
            logout(request)
            return redirect('/accounts/sign_up')
    elif request.method == 'POST':
        pattern.delete()
        return redirect('/patterns')