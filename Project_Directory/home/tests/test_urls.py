# test_urls.py



from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import *
from django.contrib.auth import views as auth_views


class testUrls(SimpleTestCase):
	
	def test_home_url_resolves(self):
		url = reverse('home')
		self.assertEquals(resolve(url).func, home)

	def test_register_url_resolves(self):
		url = reverse('register')
		self.assertEquals(resolve(url).func, register)

	def test_login_url_resolves(self):
		url = reverse('login')
		self.assertEquals(resolve(url).func, login_view)

	def test_logout_url_resolves(self):
		url = reverse('logout')
		self.assertEquals(resolve(url).func,logout_view)
