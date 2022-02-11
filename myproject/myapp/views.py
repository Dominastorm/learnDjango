from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already registered")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                messages.info(request, "User created")
                return redirect('login')
        else:
            messages.info(request, "Password not matching")
            return redirect('register')
    else:
        return render(request, 'register.html')
        
        

def counter(request):
    text = request.POST['text']
    word_count = len(text.split())
    return render(request, 'counter.html', {'word_count': word_count})