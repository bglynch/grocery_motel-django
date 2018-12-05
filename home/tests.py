from django.test import TestCase
from django.apps import apps
from django.urls import resolve
from django.contrib.auth.models import User
from .views import get_home
from .apps import HomeConfig


class TestHomeViews(TestCase):
    '''Tests for the home.view.py file'''
    
    def test_root_working_viedUsed_templateUsed(self):
        '''Tests the home(root) url.
        Check that it returns a 200 status code
        Check that it uses the correct view
        Check that it uses the correct jinja template
        '''
        found = resolve('/')  
        page = self.client.get("/")
        
        self.assertEqual(page.status_code, 200)
        self.assertEqual(found.func, get_home)
        self.assertTemplateUsed(page, 'home/home.html')  
    
    
    def test_navbar_for_logged_in_user(self):
        '''Test users home page options when user is logged in'''
        User.objects.create_user(
            username="benji",
            email="benji@ex.com",
            password="h3!!oPass"
            )
        self.client.login(username='benji', password='h3!!oPass')
        response = self.client.get('/') 
        html = response.content.decode('utf8')  
        
        self.assertIn('My Account', html)
        self.assertIn('Logout', html)
        self.assertNotIn('Login', html)  
        self.assertNotIn('Register', html)
    
    
    def test_navbar_for_logged_out_user(self):
        '''Test users home page options when user is not logged in'''
        response = self.client.get('/') 
        html = response.content.decode('utf8')  
        
        self.assertIn('Login', html)  
        self.assertIn('Register', html)
        self.assertNotIn('My Account', html)
        self.assertNotIn('Logout', html)


class TestAccountsApps(TestCase):
    '''Testing the apps.py file'''    
    
    def test_apps(self):
        self.assertEqual(HomeConfig.name, 'home')
        self.assertEqual(apps.get_app_config('home').name, 'home')
        