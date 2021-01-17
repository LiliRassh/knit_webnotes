from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.core.paginator import Paginator


def index(request):
    data = dict()
    # data['user'] = 'temp_admin'         # Временный пользователь (до вкл.авторизации)
    data['title'] = 'Связанные образцы'
    # all_webnotes = Webnote.objects.all()
    # data['notes'] = all_webnotes
    #
    # paginator = Paginator(all_webnotes, 2)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    # data['page_obj'] = page_obj

    return render(request, 'samples/index.html', context=data)


def create(request):
    data = dict()
    data['title'] = 'Добавлени записи о связанном образце'
    return render(request, 'samples/create.html', context=data)
    # if request.method == 'GET':
    #     # Блокировка доступа через адресную строку
    #     # superadmim1 : 777sssL
    #     if request.user.username == 'superadmim1':
    #         data['form_webnote'] = WebnoteForm()
    #         return render(request, 'webnotes/create.html', context=data)
    #     else:
    #         logout(request)
    #         return redirect('/accounts/sign_up')
    # elif request.method == 'POST':
    #     filled_form = WebnoteForm(request.POST, request.FILES)
    #     filled_form.save()
    #     # перенаправляем на страничку webnotes, а там запись добовляется в список со всеми записями
    #     return redirect('/webnotes')


def details(request, webnote_id):
    data = dict()
    data['title'] = 'Информация об образце'
    # data['webnote'] = Webnote.objects.get(id=webnote_id)                  # получаем id нужной новости
    return render(request, 'samples/details.html', context=data)


def edit(request, webnote_id):
    data = dict()
    data['title'] = 'Редактирование образца'
    return render(request, 'samples/edit.html', context=data)
    # webnote = Webnote.objects.get(id=webnote_id)
    # if request.method == 'GET':
    #
    #     if request.user.username == 'superadmim1':
    #         data['form'] = WebnoteForm2(instance=webnote)
    #         data['webnote'] = webnote
    #         return render(request, 'webnotes/edit.html', context=data)
    #     else:
    #         logout(request)
    #         return redirect('/accounts/sign_up')
    # elif request.method == 'POST':
    #     form2 = WebnoteForm2(request.POST)
    #     if form2.is_valid():
    #         webnote.project_name = form2.cleaned_data['project_name']
    #         webnote.start_date = form2.cleaned_data['start_date']
    #         webnote.end_date = form2.cleaned_data['end_date']
    #         webnote.for_who = form2.cleaned_data['for_who']
    #         webnote.craft = form2.cleaned_data['craft']
    #         webnote.note = form2.cleaned_data['note']
    #         webnote.private_status = form2.cleaned_data['private_status']
    #         webnote.status = form2.cleaned_data['status']
    #         webnote.save()
    #     return redirect('/webnotes')


def delete(request, webnote_id):
    data = dict()
    data['title'] = 'Удаление образца'
    return render(request, 'samples/delete.html', context=data)
    # webnote = Webnote.objects.get(id=webnote_id)
    # if request.method == 'GET':
    #     # Блокировка доступа через адресную строку
    #     if request.user.username == 'superadmim1':
    #         data['webnote'] = webnote
    #         return render(request, 'webnotes/delete.html', context=data)
    #     else:
    #         logout(request)
    #         return redirect('/accounts/sign_up')
    # elif request.method == 'POST':
    #     webnote.delete()
    #     return redirect('/webnotes')
