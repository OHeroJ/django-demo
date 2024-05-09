from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponse("wellcome")
            else:
                return HttpResponse("sorry. your username or password is wrong")
        else:
            return HttpResponse("Invalid login")
        
    login_form = LoginForm();
    return render(request, 'accounts/login.html', {'form': login_form})
        