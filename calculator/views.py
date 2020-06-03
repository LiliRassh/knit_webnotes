from django.shortcuts import render


def index(request):
    data = dict()
    data['title'] = 'Калькулятор для расчетов'
    return render(request, 'calculator/index.html', context=data)


def number_rows(request):
    data = dict()
    data['title'] = 'Расчет количества рядов'
    return render(request, 'calculator/rows.html', context=data)


def number_stitches(request):
    data = dict()
    data['title'] = 'Расчет количества петель'
    return render(request, 'calculator/stitches.html', context=data)


def rapport(request):
    data = dict()
    data['title'] = 'Расчет раппорта'
    return render(request, 'calculator/rapport.html', context=data)
