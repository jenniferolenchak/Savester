from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.

def home(request):
	return render(request, 'Home/index.html')

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Account was created')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'Home/register.html', {'form': form})


def login_view(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password incorrect')
	return render(request, 'Home/login.html')

def logout(request):
	return HttpResponse("Logout")
