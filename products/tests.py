from django.test import TestCase
from django.apps import apps
from .apps import ProductsConfig
from .models import BaseProduct


class TestProductsViews(TestCase):
    '''Testing the views.py file'''
     
    def test_get_products_page(self):
        page = self.client.get("/products/")
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products/index.html")   


class TestProductsModels(TestCase):
    '''Testing the Models in the models.py file'''
   
    def test_BaseProduct_Model(self):
        item=BaseProduct(name="Pear", price=3.22, image='file.jpg')
        item.save()
        self.assertEqual(item.__str__(), 'Pear') 


class TestProductsApps(TestCase):
    '''Testing the apps.py file'''    
    
    def test_apps(self):
        self.assertEqual(ProductsConfig.name, 'products')
        self.assertEqual(apps.get_app_config('products').name, 'products')
