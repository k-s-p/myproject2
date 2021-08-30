from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'title': 'タイトルやで！'
    }
    return render(request, 'mysite/index.html', context)