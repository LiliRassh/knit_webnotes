from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.core.paginator import Paginator
from webnotes.models import Tool
from .forms import ToolForm, ToolForm2


def index(request, user_id):
    data = dict()
    data['title'] = 'Мои инструменты'
    data['user'] = User.objects.get(id=user_id)
    if request.user.is_authenticated:
        all_tools = Tool.objects.filter(user=user_id)
        data['tools'] = all_tools
        paginator = Paginator(all_tools, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        data['page_obj'] = page_obj
        return render(request, 'tools/index.html', context=data)
    else:
        logout(request)
        return redirect('/accounts/sign_up')


def create(request):
    data = dict()
    data['title'] = 'Добавление инструмента'
    if request.method == 'GET':
        # Блокировка доступа через адресную строку
        if request.user.is_authenticated:
            data['form_tool'] = ToolForm()
            return render(request, 'tools/create.html', context=data)
        else:
            logout(request)
            return redirect('/accounts/sign_up')
    elif request.method == 'POST':
        filled_form = ToolForm(request.POST, request.FILES)
        filled_form.save()
        # перенаправляем на страничку tools, а там запись добовляется в список со всеми записями
        return redirect(f'/tools/{request.user.id}')

#
# def details(request, tool_id):
#     data = dict()
#     data['title'] = 'Информация об инструменте'
#     if request.method == 'GET':
#         if request.user.is_authenticated:
#             data['tool'] = Tool.objects.get(id=tool_id)
#             return render(request, 'tools/details.html', context=data)
#         else:
#             logout(request)
#             return redirect('/accounts/sign_up')
#


def edit(request, tool_id):
    data = dict()
    data['title'] = 'Редактирование информации об инструменте'
    tool = Tool.objects.get(id=tool_id)
    if request.method == 'GET':
        if request.user.is_authenticated:
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
        return redirect(f'/tools/{request.user.id}')


def delete(request, tool_id):
    data = dict()
    data['title'] = 'Удаление инструмента'
    tool = Tool.objects.get(id=tool_id)
    if request.method == 'GET':
        # Блокировка доступа через адресную строку
        if request.user.is_authenticated:
            data['tool'] = tool
            return render(request, 'tools/delete.html', context=data)
        else:
            logout(request)
            return redirect('/accounts/sign_up')
    elif request.method == 'POST':
        tool.delete()
        return redirect(f'/tools/{request.user.id}')
