from django.db import models
from horusmonitorweb.accounts.models import User

class Machine(models.Model):
	user       = models.ForeignKey(User)
	name       = models.CharField('Nome', max_length=50,null=False, blank=False, unique=True)
	token      = models.UUIDField(editable=False, unique=True)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)

class CPU(models.Model):
 	architecture = models.CharField('Arquitetura', max_length=100)
 	vendor_id    = models.CharField('Vendor', max_length=100)
 	model_name   = models.CharField('Modelo', max_length=100)
 	cpu_cores    = models.IntegerField('CPU cores', default=0)
 	percent_used = models.DecimalField('Percentual Utilizado',default=0.0, max_digits=5, decimal_places=2)
 	machine      = models.ForeignKey(Machine, blank=True, null=True)
 	inserted_at  = models.DateTimeField('Inserido em', blank=True, null=True, auto_now_add=True)

class OS(models.Model):
	distributor_id = models.CharField('Distribuição', max_length=100)
	release        = models.CharField('Release', max_length=100)
	codename       = models.CharField('Codename', max_length=100)
	description    = models.CharField('Descrição', max_length=100)
	machine        = models.OneToOneField(Machine, blank=True, null=True)
	inserted_at    = models.DateTimeField('Inserido em', blank=True, null=True, auto_now_add=True)

class Memory(models.Model):
	total        = models.DecimalField('Total', max_digits=5, decimal_places=2)
	used         = models.DecimalField('Utilizado', max_digits=5, decimal_places=2)
	free         = models.DecimalField('Livre', max_digits=5, decimal_places=2)
	percent_used = models.DecimalField('Percentual Utilizado', max_digits=5, decimal_places=2)
	machine      = models.ForeignKey(Machine, blank=True, null=True)
	inserted_at  = models.DateTimeField('Inserido em', blank=True, null=True, auto_now_add=True)

class Disc(models.Model):
	file_system  = models.CharField('Sistema de arquivos', max_length=100)
	size         = models.CharField('Tamanho', max_length=100)
	used         = models.CharField('Utilizado', max_length=100)
	free         = models.CharField('Livre', max_length=100)
	free_percent = models.DecimalField('Percentual Livre', max_digits=5, decimal_places=2)
	mounted_in   = models.CharField('Montado em', max_length=100)
	machine      =  models.ForeignKey(Machine, blank=True, null=True)
	inserted_at  = models.DateTimeField('Inserido em', blank=True, null=True, auto_now_add=True)
	updated_at   = models.DateTimeField('Atualizado em', blank=True, null=True, auto_now=True)

class Service(models.Model):
	STATUS_CHOICES = (
		(1, 'Running'),
		(2, 'Stopped'),
		)
	name        = models.CharField('Nome', max_length=100)
	status      = models.IntegerField('Status',choices=STATUS_CHOICES)
	machine     = models.ForeignKey(Machine, blank=True, null=True)
	inserted_at = models.DateTimeField('Inserido em', blank=True, null=True, auto_now_add=True)
	updated_at  = models.DateTimeField('Atualizado em', blank=True, null=True, auto_now=True)

class CPUAlert(models.Model):
	ALERT_CHOICES = (
		(1,'Warning'),
		(2,'Critical') 
		)
	alert_level = models.IntegerField('Nível de alerta',choices=ALERT_CHOICES, null = True)
	percent_used = models.DecimalField('Percentual Utilizado',default=0.0, max_digits=5, decimal_places=2)
	machine    = models.ForeignKey(Machine, blank=True, null=True)
	inserted_at = models.DateTimeField('Inserido em', blank=True, null=True, auto_now_add=True)

class MemoryAlert(models.Model):
	ALERT_CHOICES = (
		(1,'Warning'),
		(2,'Critical') 
		)
	alert_level = models.IntegerField('Nível de alerta',choices=ALERT_CHOICES, null = True)
	percent_used = models.DecimalField('Percentual Utilizado',default=0.0, max_digits=5, decimal_places=2)
	machine    = models.ForeignKey(Machine, blank=True, null=True)
	inserted_at = models.DateTimeField('Inserido em', blank=True, null=True, auto_now_add=True)

class DiscAlert(models.Model):
	ALERT_CHOICES = (
		(1,'Warning'),
		(2,'Critical') 
		)
	alert_level = models.IntegerField('Nível de alerta',choices=ALERT_CHOICES, null = True)
	percent_used = models.DecimalField('Percentual Utilizado',default=0.0, max_digits=5, decimal_places=2)
	partition = models.CharField('Partição', max_length=100)
	machine    = models.ForeignKey(Machine, blank=True, null=True)
	inserted_at = models.DateTimeField('Inserido em', blank=True, null=True, auto_now_add=True)

class AlertConfig(models.Model):
	ALERT_TYPES = (
		(1,'CPU'),
		(2, 'Memory'),
		(3, 'Disc')
		)
	max_warning = models.DecimalField('Máximo Atenção', max_digits=5, decimal_places=2)
	max_critical = models.DecimalField('Máximo Critico', max_digits=5, decimal_places=2)
	alert_type = models.IntegerField('Tipo de Alerta',choices=ALERT_TYPES)
	machine = models.ForeignKey(Machine, blank=True, null=True)

	class Meta:
		unique_together = ('alert_type', 'machine',)