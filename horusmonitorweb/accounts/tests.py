from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from horusmonitorweb.accounts.models import User
from horusmonitorweb.accounts.forms import RegisterForm



class RegisterFormTest(TestCase):

	def setUp(self):
		self.user = User.objects.create_user('test', 'test@testmail.com', 'testpassword')

	def tearDown(self):
		self.user.delete()

	def test_register_form_error(self):
		client = Client()
		data = {'username':'', 'email':'', 'password1':'' , 'password2':''}
		path = reverse('accounts:register')
		response = client.post(path,data)
		self.assertFormError(response, 'form', 'username', 'This field is required.')
		self.assertFormError(response, 'form', 'email', 'This field is required.')
		self.assertFormError(response, 'form', 'password1', 'This field is required.')
		self.assertFormError(response, 'form', 'password2', 'This field is required.')
	
	def test_password_confirm_error(self):
		client = Client()
		data = {'username':'test', 'email':'test@validmail.com', 'password1':'123' , 'password2':'1234'}
		path = reverse('accounts:register')
		response = client.post(path,data)
		self.assertFormError(response, 'form', 'password2', 'A confirmação não está correta')

	def test_invalid_email_error(self):
		client = Client()
		data = {'username':'test', 'email':'test@invalid', 'password1':'123' , 'password2':'123'}
		path = reverse('accounts:register')
		response = client.post(path,data)
		self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')

	def test_username_exists_error(self):
		client = Client()
		data = {'username':'test', 'email':'test@validemail.com', 'password1':'123' , 'password2':'123'}
		path = reverse('accounts:register')
		response = client.post(path,data)
		self.assertFormError(response, 'form', 'username', 'Usuário with this Nome de Usuário already exists.')

	def test_register_form_success(self):
		form_data = {'username':'test1', 'email':'test@validemail.com', 'password1':'123' , 'password2':'123'}
		form = RegisterForm(data=form_data)
		self.assertTrue(form.is_valid())

class AuthenticationTest(TestCase):

	def setUp(self):
		self.user = User.objects.create_user('test', 'test@testmail.com', 'testpassword')

	def tearDown(self):
		self.user.delete()

	def test_login_error(self):
		client = Client()
		data = {'username':'', 'password':''}
		path = reverse('accounts:login')
		response = client.post(path,data)
		self.assertContains(response, "Usuário ou senha incorretos")

	def test_login_success(self):
		client = Client()
		data = {'username':'test', 'password':'testpassword'}
		path = reverse('accounts:login')
		response = client.post(path,data)
		self.assertEqual(int(client.session['_auth_user_id']), self.user.pk)
		