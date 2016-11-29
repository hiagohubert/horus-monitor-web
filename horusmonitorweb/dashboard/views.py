from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from uuid import uuid4
from django.contrib.auth.decorators import login_required
from .forms import CreateServer, AlertConfig
from .models import Machine,OS


# Create your views here.
@login_required
def dashboard(request):
	machines = Machine.objects.filter(user=request.user)
	context = {}
	context['machines'] = machines
	return render(request, 'dashboard/index.html', context)

@login_required
def addserver(request):
	template_name = 'dashboard/addserver.html'
	context = {}
	if request.method == 'POST':
		form = CreateServer(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.user = request.user
			obj.token = uuid4()
			obj.save()
			context['success'] = True
			context['token'] = str(obj.token).replace('-','')
			#form.save()
	else:
		form = CreateServer()
	context['form'] = form
	return render(request, template_name, context)

@login_required
def server_dashboard(request, machineid):
	machine = get_object_or_404(Machine, id=machineid, user=request.user)
	context = {}
	context['machine'] = machine
	return render(request, 'dashboard/dashboard.html', context)

@login_required
def server_discs(request, machineid):
	machine = get_object_or_404(Machine, id=machineid, user=request.user)
	context = {}
	context['machine'] = machine
	return render(request, 'dashboard/discs.html', context)

@login_required
def server_services(request, machineid):
	machine = get_object_or_404(Machine, id=machineid, user=request.user)
	context = {}
	context['machine'] = machine
	return render(request, 'dashboard/services.html', context)

@login_required
def cpu_today(request, machineid):
	machine = get_object_or_404(Machine, id=machineid, user=request.user)
	context = {}
	context['machine'] = machine
	return render(request, 'dashboard/cpu_today.html', context)

@login_required
def memory_today(request, machineid):
	machine = get_object_or_404(Machine, id=machineid, user=request.user)
	context = {}
	context['machine'] = machine
	return render(request, 'dashboard/memory_today.html', context)

@login_required
def alert_config(request, machineid):
	machine = get_object_or_404(Machine, id=machineid, user=request.user)
	context = {}
	if request.method == 'POST':
		form = AlertConfig(request.POST)
		if form.is_valid():
			obj = form.save(commit = False)
			obj.machine = machine
			obj.save()
			context['success'] = True
	else:
		form = AlertConfig()

	context['form'] = form
	context['machine'] = machine
	return render(request, 'dashboard/alert_config.html', context)

@login_required
def alert_config_list(request, machineid):
	machine = get_object_or_404(Machine, id=machineid, user=request.user)
	context = {}
	context['machine'] = machine
	
	if request.method == 'GET' and request.GET.get('id_alert') != None and request.GET.get('a') == 'del' :
		instance = machine.alertconfig_set.get(id=request.GET.get('id_alert'))
		instance.delete()


	return render(request, 'dashboard/list_alerts.html', context)
