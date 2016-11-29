from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
# Create your tests here.

class HomeTestView(TestCase):
	
	def test_home_status_code(self):
		client = Client()
		response = client.get(reverse('core:home'))
		self.assertEquals(response.status_code, 200)

	def test_home_template_used(self):
		client = Client()
		response = client.get(reverse('core:home'))
		self.assertTemplateUsed(response, 'home.html')

		