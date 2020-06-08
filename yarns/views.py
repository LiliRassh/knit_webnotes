from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from webnotes.models import Yarn
from .forms import YarnForm, YarnForm2
from django.contrib.auth import logout
from django.core.paginator import Paginator


def index(request, user_id):
    data = dict()
    data['title'] = 'Моя пряжа'
    user = get_object_or_404(User, id=user_id)
    data['user'] = user
    if request.method == 'GET':
        if request.user.is_authenticated:
            all_yarns = Yarn.objects.filter(user=user_id)
            data['yarns'] = all_yarns
            paginator = Paginator(all_yarns, 3)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            data['page_obj'] = page_obj

            return render(request, 'yarns/index.html', context=data)
        else:
            logout(request)
            return redirect('/accounts/sign_up')


def create(request):
    data = dict()
    data['title'] = 'Добавление пряжи'
    if request.method == 'GET':
        # Блокировка доступа через адресную строку
        # superadmim1 : 777sssL
        if request.user.is_authenticated:
            data['form_yarn'] = YarnForm()
            print(data['form_yarn'])
            return render(request, 'yarns/create.html', context=data)
        else:
            logout(request)
            return redirect('/accounts/sign_up')
    elif request.method == 'POST':
        filled_form = YarnForm(request.POST, request.FILES)
        print(filled_form.data)
        filled_form.save()
        # перенаправляем на страничку yarns/index.html, а там запись добовляется в список со всеми записями
        return redirect(f'/yarns/{request.user.id}')

#
# def details(request, yarn_id):
#     data = dict()
#     data['title'] = 'Информация о пряже'
#     if request.method == 'GET':
#         if request.user.is_authenticated:
#             data['yarn'] = Yarn.objects.get(id=yarn_id)
#             return render(request, 'yarns/details.html', context=data)
#         else:
#             logout(request)
#             return redirect('/accounts/sign_up')
#


def edit(request, yarn_id):
    data = dict()
    data['title'] = 'Редактирование информации о пряже'
    yarn = Yarn.objects.get(id=yarn_id)
    if request.method == 'GET':
        if request.user.is_authenticated:
            data['form'] = YarnForm2(instance=yarn)
            data['yarn'] = yarn
            return render(request, 'yarns/edit.html', context=data)
        else:
            logout(request)
            return redirect('/accounts/sign_up')
    elif request.method == 'POST':
        form2 = YarnForm2(request.POST)
        if form2.is_valid():
            yarn.name = form2.cleaned_data['name']
            yarn.color_lot = form2.cleaned_data['color_lot']
            yarn.weight = form2.cleaned_data['weight']
            yarn.length = form2.cleaned_data['length']
            yarn.label = form2.cleaned_data['label']
            yarn.source = form2.cleaned_data['source']
            yarn.save()
        return redirect(f'/yarns/{request.user.id}')


def delete(request, yarn_id):
    data = dict()
    data['title'] = 'Удалить пряжу'
    yarn = Yarn.objects.get(id=yarn_id)
    if request.method == 'GET':
        # Блокировка доступа через адресную строку
        if request.user.is_authenticated:
            data['yarn'] = yarn
            return render(request, 'yarns/delete.html', context=data)
        else:
            logout(request)
            return redirect('/accounts/sign_up')
    elif request.method == 'POST':
        yarn.delete()
        return redirect(f'/yarns/{request.user.id}')

