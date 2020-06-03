from django.shortcuts import render, redirect
from webnotes.models import Tool
from .forms import ToolForm, ToolForm2
from django.contrib.auth import logout
# from django.core.paginator import Paginator


def index(request):
    data = dict()
    # data['user'] = 'temp_admin'         # Временный пользователь (до вкл.авторизации)
    data['title'] = 'Мои инструменты'
    all_tools = Tool.objects.all()
    data['tools'] = all_tools
    return render(request, 'tools/index.html', context=data)
    #
    # paginator = Paginator(all_webnotes, 2)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    # data['page_obj'] = page_obj


def create(request):
    data = dict()
    data['title'] = 'Добавление инструмента'
    if request.method == 'GET':
        # Блокировка доступа через адресную строку
        # superadmim1 : 777sssL
        if request.user.username == 'superadmim1':
            data['form_tool'] = ToolForm()
            return render(request, 'tools/create.html', context=data)
        else:
            logout(request)
            return redirect('/accounts/sign_up')
    elif request.method == 'POST':
        filled_form = ToolForm(request.POST, request.FILES)
        filled_form.save()
        # перенаправляем на страничку tools, а там запись добовляется в список со всеми записями
        return redirect('/tools')


def details(request, tool_id):
    data = dict()
    data['title'] = 'Информация об инструменте'
    data['tool'] = Tool.objects.get(id=tool_id)                  # получаем id нужной новости
    return render(request, 'tools/details.html', context=data)


def edit(request, tool_id):
    data = dict()
    data['title'] = 'Редактирование информации об инструменте'
    tool = Tool.objects.get(id=tool_id)
    if request.method == 'GET':
        if request.user.username == 'superadmim1':
            data['form'] = ToolForm2(instance=tool)
            data['tool'] = tool
            return render(request, 'tools/edit.html', context=data)
        else:
            logout(request)
            return redirect('/accounts/sign_up')
    elif request.method == 'POST':
        form2 = ToolForm2(request.POST)
        if form2.is_valid():
            tool.name = form2.cleaned_data['name']
            tool.size = form2.cleaned_data['size']
            tool.producer = form2.cleaned_data['producer']
            tool.type = form2.cleaned_data['type']
            tool.material = form2.cleaned_data['material']
            tool.save()
        return redirect('/tools')


def delete(request, tool_id):
    data = dict()
    data['title'] = 'Удаление инструмента'
    tool = Tool.objects.get(id=tool_id)
    if request.method == 'GET':
        # Блокировка доступа через адресную строку
        if request.user.username == 'superadmim1':
            data['tool'] = tool
            return render(request, 'tools/delete.html', context=data)
        else:
            logout(request)
            return redirect('/accounts/sign_up')
    elif request.method == 'POST':
        tool.delete()
        return redirect('/tools')
