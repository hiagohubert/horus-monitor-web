from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import MachineSerializer, OSSerializer, CPUSerializer, MemorySerializer, DiscSerializer, ServiceSerializer
from django.views.decorators.csrf import csrf_exempt
from horusmonitorweb.dashboard.models import Machine, Disc, Service, CPU, Memory, CPUAlert, MemoryAlert, DiscAlert
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
import datetime
from decimal import Decimal
from django.core.mail import send_mail
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


# Create your views here.
@csrf_exempt
@api_view(['GET'])
def machine_detail(request, token):
	try:
		machine = Machine.objects.get(token=token)
	except Machine.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = MachineSerializer(machine)
		return JSONResponse(serializer.data)

@api_view(['POST'])
def os_info(request):
	if request.method == 'POST':
		req = request.POST.copy()
		try:
			machine = Machine.objects.get(token=req['token'])
			print (req['token'])
		except Machine.DoesNotExist:
			return HttpResponse(status=404)
		req['machine'] = machine.id
		serializer = OSSerializer(data=req)
		if serializer.is_valid():
			serializer.save()
			return HttpResponse(status=200)
		else:
			return HttpResponse(status=500)

@api_view(['POST', 'GET'])
def cpu_info(request):
	if request.method == 'POST':
		req = request.POST.copy()
		try:
			machine = Machine.objects.get(token=req['token'])
			alertCPU(req['percent_used'], machine)
		except Machine.DoesNotExist:
			return HttpResponse(status=404)
		req['machine'] = machine.id
		serializer = CPUSerializer(data=req)
		if serializer.is_valid():
			serializer.save()
			return HttpResponse(status=200)
		else:
			return HttpResponse(status=500)

   # example /api/cpu/?start_date=2016-05-23&end_date=2016-05-24&machine=1 - Data especific
   # example /api/cpu/?machine=1 - Today
	elif request.method =='GET':
		try:
			machine = Machine.objects.get(id=request.GET.get('machine'), user=request.user )
		except Machine.DoesNotExist:
			return HttpResponse(status=400)

		try:
			if request.GET.get('start_date') != None and request.GET.get('end_date') != None:
				start_date = datetime.datetime.strptime(request.GET.get('start_date',''), '%Y-%m-%d %H:%M:%S')
				end_date = datetime.datetime.strptime(request.GET.get('end_date',''), '%Y-%m-%d %H:%M:%S')
			else:
				date = datetime.datetime.today()
				newdate = date.replace(hour=00, minute=00, second=00, microsecond=00)
				start_date = newdate
				end_date = date

			cpu = CPU.objects.filter(machine=request.GET.get('machine',''), inserted_at__range=(start_date,end_date))
			serializer = CPUSerializer(cpu, many=True)
			return JSONResponse(serializer.data)
		except CPU.DoesNotExist:
			return HttpResponse(status=404) 

@api_view(['POST', 'GET'])
def memory_info(request):
	if request.method == 'POST':
		req = request.POST.copy()
		try:
			machine = Machine.objects.get(token=req['token'])
			alertMemory(req['percent_used'], machine)
		except Machine.DoesNotExist:
			return HttpResponse(status=404)
		req['machine'] = machine.id
		serializer = MemorySerializer(data=req)
		if serializer.is_valid():
			serializer.save()
			return HttpResponse(status=200)
		else:
			return HttpResponse(status=500)

	elif request.method == 'GET':
		try:
			machine = Machine.objects.get(id=request.GET.get('machine'), user=request.user )
		except Machine.DoesNotExist:
			return HttpResponse(status=400)
		try:
			if request.GET.get('start_date') != None and request.GET.get('end_date') != None:
				start_date = datetime.datetime.strptime(request.GET.get('start_date',''), '%Y-%m-%d %H:%M:%S')
				end_date = datetime.datetime.strptime(request.GET.get('end_date',''), '%Y-%m-%d %H:%M:%S')
			else:
				date = datetime.datetime.today()
				newdate = date.replace(hour=00, minute=00, second=00, microsecond=00)
				start_date = newdate
				end_date = date

			memory = Memory.objects.filter(machine=request.GET.get('machine',''), inserted_at__range=(start_date,end_date))
			serializer = MemorySerializer(memory, many=True)
			return JSONResponse(serializer.data)
		except Memory.DoesNotExist:
			return HttpResponse(status=404)



@api_view(['POST'])
def disc_info(request):
	if request.method == 'POST':
		req = request.POST.copy()
		try:
			machine = Machine.objects.get(token=req['token'])
			req['machine'] = machine.id
			alertDisc(req['free_percent'], req['mounted_in'], machine)
		except Machine.DoesNotExist:
			return HttpResponse(status=404)
		try:
			disc = Disc.objects.get(machine=machine.id,mounted_in=req['mounted_in'])
		except Disc.DoesNotExist:
			serializer = DiscSerializer(data=req)
		else:
			serializer = DiscSerializer(disc ,data=req)
		if serializer.is_valid():
			serializer.save()
			return HttpResponse(status=200)
		else:
			return HttpResponse(status=500)

@api_view(['POST'])
def service_info(request):
	if request.method == 'POST':
		req = request.POST.copy()
		try:
			machine = Machine.objects.get(token=req['token'])
			req['machine'] = machine.id
		except Machine.DoesNotExist:
			return HttpResponse(status=404)
		try:
			service = Service.objects.get(machine=machine.id,name=req['name'])
		except Service.DoesNotExist:
			serializer = ServiceSerializer(data=req)
		else:
			serializer = ServiceSerializer(service ,data=req)
		if serializer.is_valid():
			serializer.save()
			return HttpResponse(status=200)
		else:
			return HttpResponse(status=500)


def send_alert(subject, email, message):
    subject = subject
    message = message
    send_mail(
        subject, message, settings.DEFAULT_FROM_EMAIL, 
        [email]
        )

def alertCPU(percent_used, machine):
	try:
		alertconfig = machine.alertconfig_set.get(alert_type=1)
		if Decimal(percent_used) >= alertconfig.max_warning and Decimal(percent_used) < alertconfig.max_critical:
			instance = CPUAlert(alert_level=1, machine=machine, percent_used=Decimal(percent_used))
			instance.save()
			send_alert("[Horus Monitor] Alerta Atenção: Uso de "+percent_used+"% de CPU no servidor", machine.user.email, 'Foi detectado o uso de '+percent_used+'% de CPU no servidor')
		elif Decimal(percent_used) >= alertconfig.max_critical :
			instance = CPUAlert(alert_level=2, machine=machine, percent_used=Decimal(percent_used))
			instance.save()
			send_alert("[Horus Monitor] Alerta Crítico: Uso de "+percent_used+"% de CPU no servidor", machine.user.email, 'Foi detectado o uso de '+percent_used+'% de CPU no servidor')
	except ObjectDoesNotExist:
				pass

def alertMemory(percent_used,machine):
	try:
		alertconfig = machine.alertconfig_set.get(alert_type=2)
		if Decimal(percent_used) >= alertconfig.max_warning and Decimal(percent_used) < alertconfig.max_critical:
			instance = MemoryAlert(alert_level=1, machine=machine, percent_used=Decimal(percent_used))
			instance.save()
			send_alert("[Horus Monitor] Alerta Atenção: Uso de "+percent_used+"% de Memória no servidor", machine.user.email, 'Foi detectado o uso de '+percent_used+'% de Memória no servidor')
		elif Decimal(percent_used) >= alertconfig.max_critical :
			instance = MemoryAlert(alert_level=2, machine=machine, percent_used=Decimal(percent_used))
			instance.save()
			send_alert("[Horus Monitor] Alerta Crítico: Uso de "+percent_used+"% de Memória no servidor", machine.user.email, 'Foi detectado o uso de '+req['percent_used']+'% de Memória no servidor')

	except ObjectDoesNotExist:
		pass

def alertDisc(free_percent, mounted_in, machine):
	try:
		alertconfig = machine.alertconfig_set.get(alert_type=3)
		percent_used = 100.0 - float(free_percent)
		if percent_used >= alertconfig.max_warning and percent_used < alertconfig.max_critical:
		   instance = DiscAlert(alert_level=1,partition=mounted_in, machine=machine, percent_used=percent_used)
		   instance.save()
		   send_alert("[Horus Monitor] Alerta Atenção: Uso de "+str(percent_used)+"% de Disco na partição "+mounted_in+" no servidor", machine.user.email, 'Foi detectado o uso de '+str(percent_used)+'% de Disco no servidor')		   			
		elif percent_used >= alertconfig.max_critical :
		   instance = DiscAlert(alert_level=2, partition=mounted_in,  machine=machine, percent_used=Decimal(req['percent_used']))
		   instance.save()
		   send_alert("[Horus Monitor] Alerta Crítico: Uso de "+percent_used+"% de Disco na partição "+mounted_in+" no servidor", machine.user.email, 'Foi detectado o uso de '+str(percent_used)+'% de Disco no servidor')

	except ObjectDoesNotExist:
		pass