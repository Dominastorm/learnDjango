from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def counter(request):
    text = request.POST['text']
    word_count = len(text.split())
    return render(request, 'counter.html', {'word_count': word_count})