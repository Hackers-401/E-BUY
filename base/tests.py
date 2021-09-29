from django.test import TestCase
from base import products
from base.models import Product

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.http import response
from django.contrib.auth.models import User
from base.models import *

# Create your tests here.

class AllProductTests(APITestCase):

    def test_view_products(self):

        url = reverse('products')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        
    def test__is_order_not_Unauthorized(self):

        url = reverse('orders')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)      


class Test_Create_Product(TestCase):


    @classmethod
    def setUpTestData(cls):
        
        testuser1 = User.objects.create(
            username = "testuser1" , password='123456789'
        )
        test_product=Product.objects.create(name="hp2020"  , brand="hp" ,category="laptop" , description="good" , price=800)   

    def test_product_content(self):
        product = Product.productobjects.get(_id=1)

        name=f'{product.name}'
       
        brand=f'{product.brand}'
        category=f'{product.category}'
        description=f'{product.description}'
        price=f'{product.price}'

        self.assertEqual(name , "hp2020")
        
        self.assertEqual(brand , "hp")
        self.assertEqual(category , "laptop")
        self.assertEqual(description , "good")
        self.assertEqual(price , "800.00")