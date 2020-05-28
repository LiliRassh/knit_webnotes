from django.shortcuts import render, redirect
from .models import Notes, Status, Tools, Pattern, Yarn
from .forms import NotesForm, NotesForm2, ToolsForm, PatternForm, YarnForm
from django.contrib.auth import logout
from django.core.paginator import Paginator


def index(request):
    data = dict()
    # data['user'] = 'temp_admin'         # Временный пользователь (до вкл.авторизации)
    data['title'] = 'Твой Веб-блокнот'
    all_notes = Notes.objects.all()
    data['notes'] = all_notes

    paginator = Paginator(all_notes, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data['page_obj'] = page_obj

    return render(request, 'webnotes/index.html', context=data)


def create(request):
    data = dict()
    data['title'] = 'Создание записи в Веб-блокноте'
    if request.method == 'GET':
        # Блокировка доступа через адресную строку
        # superadmim1 : 777sssL
        if request.user.username == 'superadmim1':
            data['form_notes'] = NotesForm()
            return render(request, 'webnotes/create.html', context=data)
        else:
            logout(request)
            return redirect('/accounts/sign_up')
    elif request.method == 'POST':
        filled_form = NotesForm(request.POST, request.FILES)
        filled_form.save()
        # перенаправляем на страничку webnotes, а там запись добовляется в список со всеми записями
        return redirect('/webnotes')


def details(request, notes_id):
    data = dict()
    data['title'] = 'Просмотр записи о проекте'
    data['notes'] = Notes.objects.get(id=notes_id)                  # получаем id нужной новости
    return render(request, 'webnotes/details.html', context=data)


def edit(request, notes_id):
    data = dict()
    data['title'] = 'Редактирование записи в Веб-блокноте'
    notes = Notes.objects.get(id=notes_id)
    if request.method == 'GET':

        if request.user.username == 'superadmim1':
            data['form'] = NotesForm2(instance=notes)
            data['notes'] = notes
            return render(request, 'webnotes/edit.html', context=data)
        else:
            logout(request)
            return redirect('/accounts/sign_up')
    elif request.method == 'POST':
        form2 = NotesForm2(request.POST)
        if form2.is_valid():
            notes.project_name = form2.cleaned_data['title']
            notes.start_date = form2.cleaned_data['start_date']
            notes.end_date = form2.cleaned_data['end_date']
            notes.for_who = form2.cleaned_data['for_who']
            notes.craft = form2.cleaned_data['craft']
            notes.note = form2.cleaned_data['note']
            notes.status = form2.cleaned_data['status']
            notes.save()
        return redirect('/webnotes')


def delete(request, notes_id):
    data = dict()
    data['title'] = 'Удаление записи о проекте из Веб-блокнота'
    notes = Notes.objects.get(id=notes_id)
    if request.method == 'GET':
        # Блокировка доступа через адресную строку
        if request.user.username == 'superadmim1':
            data['notes'] = notes
            return render(request, 'webnotes/delete.html', context=data)
        else:
            logout(request)
            return redirect('/accounts/sign_up')
    elif request.method == 'POST':
        notes.delete()
        return redirect('/webnotes')
