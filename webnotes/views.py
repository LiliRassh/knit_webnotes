from django.shortcuts import render, redirect
from .models import Webnote, Pattern, Tool, Yarn
from .forms import WebnoteForm, WebnoteForm2
from django.contrib.auth import logout
from django.core.paginator import Paginator


def index(request, user_id):
    data = dict()
    data['title'] = 'Мой Веб-блокнот'
    if request.user.is_authenticated:
        all_webnotes = Webnote.objects.filter(user=user_id)
        #
        # pat = []
        # for w in all_webnotes:
        #     pattern = Webnote.objects.get(id=w.id).pattern.all()
        #     # tool = Webnote.objects.get(id=w.id).tool.all()
        #     # yarn = Webnote.objects.get(id=w.id).yarn.all()
        #     # print(w, pattern)
        #     # pat.append(w)
        #     pat.append(pattern)
        #     # pat.append(tool)
        #     # pat.append(yarn)
        # # data['pattern'] = pat
        # print(pat)
        data['webnotes'] = all_webnotes
        # data['pattern'] = pat
    else:
        logout(request)
        return redirect('/accounts/sign_up')
    paginator = Paginator(all_webnotes, 2)
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
        if request.user.is_authenticated:
            data['form_webnote'] = WebnoteForm()
            data['form_pattern'] = Pattern.objects.filter(user=request.user.id)
            data['form_tool'] = Tool.objects.filter(user=request.user.id)
            data['form_yarn'] = Yarn.objects.filter(user=request.user.id)
            # print(data['form_pattern'], data['form_tool'], data['form_yarn'])
            return render(request, 'webnotes/create.html', context=data)
        else:
            logout(request)
            return redirect('/accounts/sign_up')
    elif request.method == 'POST':
        filled_form = WebnoteForm(request.POST, request.FILES)
        print(filled_form.data)
        filled_form.save()
        # перенаправляем на страничку webnotes
        return redirect(f'/webnotes/{request.user.id}')


def details(request, webnote_id):
    data = dict()
    data['title'] = 'Просмотр записи о проекте'
    if request.method == 'GET':
        data['webnote'] = Webnote.objects.get(id=webnote_id)
        return render(request, 'webnotes/details.html', context=data)


def edit(request, webnote_id):
    data = dict()
    data['title'] = 'Редактирование записи в Веб-блокноте'
    webnote = Webnote.objects.get(id=webnote_id)
    if request.method == 'GET':
        if request.user.is_authenticated:
            data['form'] = WebnoteForm2(instance=webnote)
            data['webnote'] = webnote
            data['form_pattern'] = Pattern.objects.filter(user=request.user.id)
            data['form_tool'] = Tool.objects.filter(user=request.user.id)
            data['form_yarn'] = Yarn.objects.filter(user=request.user.id)
            return render(request, 'webnotes/edit.html', context=data)
        else:
            logout(request)
            return redirect('/accounts/sign_up')
    elif request.method == 'POST':
        form2 = WebnoteForm2(request.POST)
        if form2.is_valid():
            webnote.project_name = form2.cleaned_data['project_name']
            webnote.start_date = form2.cleaned_data['start_date']
            webnote.end_date = form2.cleaned_data['end_date']
            webnote.for_who = form2.cleaned_data['for_who']
            webnote.craft = form2.cleaned_data['craft']
            webnote.note = form2.cleaned_data['note']
            webnote.access = form2.cleaned_data['access']
            webnote.status = form2.cleaned_data['status']
            webnote.save()
        return redirect(f'/webnotes/{request.user.id}')


def delete(request, webnote_id):
    data = dict()
    data['title'] = 'Удаление записи о проекте из Веб-блокнота'
    webnote = Webnote.objects.get(id=webnote_id)
    if request.method == 'GET':
        # Блокировка доступа через адресную строку
        if request.user.is_authenticated:
            data['webnote'] = webnote
            return render(request, 'webnotes/delete.html', context=data)
        else:
            logout(request)
            return redirect('/accounts/sign_up')
    elif request.method == 'POST':
        webnote.delete()
        return redirect(f'/webnotes/{request.user.id}')


def public(request):
    data = dict()
    data['title'] = 'Коллекция Веб-записей'
    public_webnotes = Webnote.objects.filter(access=2)
    data['webnotes'] = public_webnotes
    paginator = Paginator(public_webnotes, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data['page_obj'] = page_obj
    return render(request, 'webnotes/public.html', context=data)
