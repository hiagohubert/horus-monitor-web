from django.test import TestCase
from .models import Machine
from horusmonitorweb.accounts.models import User
from django.test.client import Client
from django.core.urlresolvers import reverse
from .forms import CreateServer, AlertConfig
from uuid import uuid4


class CreateServerTest(TestCase):

	def setUp(self):
		self.user = User.objects.create_user('test', 'test@testmail.com', 'testpassword')

	def tearDown(self):
		self.user.delete()

	def test_create_server_form_error(self):
		client = Client()
		client.login(username='test', password='testpassword')
		data = {}
		path = reverse('dashboard:addserver')
		response = client.post(path,data)
		self.assertFormError(response, 'form', 'name', 'This field is required.')

	def test_create_server_form_success(self):
		form_data = {'name': 'test'}
		form = CreateServer(data=form_data)
		self.assertTrue(form.is_valid())

class AlertConfigTest(TestCase):

	def setUp(self):
		self.user = User.objects.create_user('test', 'test@testmail.com', 'testpassword')
		self.machine = Machine.objects.create(name='test_machine', token=uuid4(), user=self.user)

	def tearDown(self):
		self.machine.delete()
		self.user.delete()
		
	def test_alert_config_form_error(self):
		client = Client()
		client.login(username='test', password='testpassword')
		data = {'max_warning':'', 'max_critical':'', 'alert_type':''}
		path = reverse('dashboard:alert_config', kwargs={'machineid': int(self.machine.id)})
		response = client.post(path,data)
		self.assertFormError(response, 'form', 'max_warning', 'This field is required.')
		self.assertFormError(response, 'form', 'max_critical', 'This field is required.')
		self.assertFormError(response, 'form', 'alert_type', 'This field is required.')

	def test_create_server_form_success(self):
		form_data = {'max_warning':'1', 'max_critical':'1', 'alert_type':'1'}
		form = AlertConfig(data=form_data)
		self.assertTrue(form.is_valid())
