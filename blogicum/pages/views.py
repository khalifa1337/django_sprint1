from django.shortcuts import render


def about(request):
    """Функция для отображения страницы 'О проекте'."""
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    """Функция для отображения страницы 'Правила'."""
    template = 'pages/rules.html'
    return render(request, template)
