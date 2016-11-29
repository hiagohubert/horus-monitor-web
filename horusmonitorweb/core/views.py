from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login
from django.template.context_processors import csrf
from horusmonitorweb.accounts.forms import RegisterForm

# Create your views here.

def home(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			user = authenticate(
				username=user.username, password=form.cleaned_data['password1']
				)
			login(request, user)
			return redirect('dashboard:index')
	else:
		form = RegisterForm()

	c = {}
	c.update(csrf(request))
	c.update({'form':form})
	return render(request, 'home.html', c)