from django.test import TestCase
from django.apps import apps
from django.urls import resolve
from django.contrib.auth.models import User
from django.http import HttpRequest
from .views import get_home
from .apps import HomeConfig

class TestHomeViews(TestCase):
    
    def test_navbar_for_non_logged_in_user(self):
        found = resolve('/')  
        page = self.client.get("/")
        
        self.assertEqual(found.func, get_home)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'home/home.html')  
    
    
    def test_navbar_for_logged_in_user(self):
        User.objects.create_user(username="benji", email="benji@ex.com", password="h3!!oPass")
        self.client.login(username='benji', password='h3!!oPass')
        response = self.client.get('/') 
        html = response.content.decode('utf8')  
        
        self.assertIn('My Account', html)
        self.assertIn('Logout', html)
        self.assertNotIn('Login', html)  
        self.assertNotIn('Register', html)


class TestAccountsApps(TestCase):
    '''Testing the apps.py file'''    
    
    def test_apps(self):
        self.assertEqual(HomeConfig.name, 'home')
        self.assertEqual(apps.get_app_config('home').name, 'home')
        