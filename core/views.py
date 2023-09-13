
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile

# Create your views here.
@login_required(login_url='signin')
def home(request):
    return render(request, 'home.html')
def profile(request):
    return render(request, 'profile.html')
@login_required(login_url='signin')
def dashboard(request):
    return render(request, 'dashboard.html')
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'EMAIL TAKEN')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'USERNAME EXISTS')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                messages.success(request, 'ACCOUNT CREATED SUCCESSFULLY NOW LOGIN')
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('signin')
        else:
            messages.info(request, 'PASSWORD DO NOT MATCH')
            return redirect('signup')


    else:

      return render(request, 'sign-up.html')
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'INVALID CREDENTIALS')
            return redirect('signin')
    else:

     return render(request, 'sign-in.html')
def billing(request):
    return render(request, 'billing.html')
def tables(request):
    return render(request, 'table.html')
def map(request):
    return render(request, 'map.html')
def typography(request):
    return render(request, 'typography.html')
def notifications(request):
    return render(request, 'notifications.html')
def template(request):
    return render(request, 'notifications.html')
@login_required(login_url='signin')
def settings(request):
    return render(request, 'setting.html')
@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    messages.info(request, 'SUCCESSFULLY LOGGED OUT')
    return redirect('signin')
