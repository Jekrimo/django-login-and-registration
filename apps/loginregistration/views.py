from django.shortcuts import render, HttpResponse, redirect
from . import models
from models import Users

def index(request):
    return render(request, 'loginreg/index.html')

def create(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirmPass']:
            info = Users.create.register(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email_address = request.POST['email'], create_password = request.POST['password'])
            if info[0]:
                request.session['user'] = request.POST['first_name']
                request.session['create'] = "registered!"
                return redirect('/success')
            else:
                return render(request, 'loginreg/index.html', context =  {'errors' : info[1]})

def login(request):
    if request.method == 'POST':
        logs = Users.login.userlogin(login_email = request.POST['login_email'], login_password = request.POST['log_password'])
        if logs[0]:
            request.session['create'] = "Logged in!"
            return redirect('/success')
        else:
            return render(request, 'loginreg/index.html', context =  {'errors' : logs[1]})

def success(request):
    context = {
        'users' : Users.objects.all()
    }
    return render(request, 'loginreg/success.html', context)
