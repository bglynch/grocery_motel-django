from django.test import TestCase
from django.apps import apps
from .forms import UserRegisterForm
from .apps import AccountsConfig


class TestAccountsForms(TestCase):
    '''Testing the forms.py file'''

    # ---------------------------------------------------Sad Path Tests

    def test_register(self):
        form = UserRegisterForm({
            'username': 'benji',
            'email': 'benji@ex.com',
            'password1': 'h3!!oPass',
            'password2': 'h3!!oPass',
        })
        self.assertTrue(form.is_valid())


    # ---------------------------------------------------Sad Path Tests

    def test_register_poor_password(self):
        form = UserRegisterForm({
            'username': 'benji',
            'email': 'benji@ex.com',
            'password1': 'password',
            'password2': 'password',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['password2'], ["This password is too common."]
            )


    def test_register_different_passwords(self):
        form = UserRegisterForm({
            'username': 'benji',
            'email': 'benji@ex.com',
            'password1': 'h3!!oPass',
            'password2': 'h3!!oPas',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['password2'], ["The two password fields didn't match."]
            )


    def test_register_bad_email(self):
        form = UserRegisterForm({
            'username': 'benji',
            'email': 'benjiex.com',
            'password1': 'h3!!oPass',
            'password2': 'h3!!oPas',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['email'], ["Enter a valid email address."]
            )


# class TestAccountsViews(TestCase):


class TestAccountsApps(TestCase):
    '''Testing the apps.py file'''    
    def test_apps(self):
        self.assertEqual(AccountsConfig.name, 'accounts')
        self.assertEqual(apps.get_app_config('accounts').name, 'accounts')