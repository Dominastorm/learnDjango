from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'name': 'Django',
        'age': '18',
        'nationality': 'indian'
    }
    return render(request, 'index.html', context)