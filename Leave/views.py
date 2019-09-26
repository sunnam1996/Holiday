from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import LeaveAppUser
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request,'home.html')


def usercreation(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            request.session['user'] = username
            return redirect('userauthentication')

    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


def userpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['user'] = username
                return redirect('userauthentication')
            messages.add_message(request, messages.INFO, 'User is Not Active.')
            return redirect('userpage')
        messages.add_message(request, messages.INFO, 'Please Check Your Login Credentials.')
        return redirect('userpage')

    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})


def userauthentication(request):
    if request.session.has_key('user'):
        username = request.session['user']
        user = LeaveAppUser.objects.get(username=username)
        if user.is_staff == True:
            return render(request, 'AdminPage.html')
        leavetype = Leavetype.objects.all()
        return render(request, 'userpage.html', {'leavetype': leavetype})
    return redirect('userpage')

