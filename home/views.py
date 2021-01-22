from django.shortcuts import render
from django.core.mail import send_mail
from webnotes.models import Webnote, Pattern


def index(request):
    data = dict()
    data['title'] = 'Главная'
    data['public_webnotes'] = Webnote.objects.filter(access=2)       # [:10]
    data['public_patterns'] = Pattern.objects.filter(webnote__access=2)
    return render(request, 'home/index.html', context=data)


def about(request):
    data = {'title': 'О сайте'}
    return render(request, 'home/about.html', context=data)


def contacts(request):
    data = dict()
    data['title'] = 'Контакты'
    # data['display'] = 'none'
    # print('test1')
    # if request.method == 'GET':
    #     data['title'] = 'Контакты'
    #     # data['send'] = False
    #     print('test2')
    #     return render(request, 'home/contacts.html', context=data)
    # elif request.method == 'POST':
    #     form = request.POST.get('contacts')
    #     email = request.POST.get('email')
    #     message = request.POST.get('message')
    #     print('test3')
    #     # if form.is_valid():
    #         # Form fields passed validation
    #     subject = 'Сообщение из формы обратной связи KnittingWebNotes'
    #     send_mail(subject, message, email, ['lili.rassh202012@gmail.com'], fail_silently=False)
    #     # data['send'] = True
    #     # Отчет о выполнении
    #     data['title'] = 'Отчет об отправке'
    #     data['color_mess'] = 'green'
    #     data['report_mess'] = 'Ваше письмо отправлено!'
    #     print('test4')
    # else:
    #     data['report_mess'] = 'Форма заполнена не правильно!'
    #     data['color'] = 'red'
    #     data['display'] = 'block'
    #     print('test5')
    #     return render(request, 'home/contacts.html', context=data)
    return render(request, 'home/success.html.html', context=data)
