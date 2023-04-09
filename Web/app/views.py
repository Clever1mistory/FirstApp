from django.shortcuts import render


def index(request):
    data = {
        'title': 'Main page'
    }
    return render(request, 'app/index.html', data)


def about(request):
    return render(request, 'app/about.html')