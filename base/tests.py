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

    def test_view_users_is_not_Unauthorized(self):

        url = reverse('users')
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
        
class Test_Create_Order(TestCase):


    @classmethod
    def setUpTestData(cls):
        
        testuser1 = User.objects.create(
            username = "testuser1" , password='123456789'
        )
        test_order=Order.objects.create(paymentMethod="paypal" , taxPrice=20 , shippingPrice=600 ,totalPrice=900 )   

    def test_order_content(self):
        order = Order.order_object.get(_id=1)

        paymentMethod=f'{order.paymentMethod}'
        taxPrice=f'{order.taxPrice}'
        shippingPrice=f'{order.shippingPrice}'
        totalPrice=f'{order.totalPrice}'
       

        self.assertEqual(paymentMethod , "paypal")
        self.assertEqual(taxPrice ,"20.00" )
        self.assertEqual(shippingPrice , "600.00")
        self.assertEqual(totalPrice , "900.00")


class Test_Create_Review(TestCase):


    @classmethod
    def setUpTestData(cls):
        
        testuser1 = User.objects.create(
            username = "testuser1" , password='123456789'
        )
        test_review=Review.objects.create(name="khaled" , rating=4 , comment="not bad")   

    def test_review_content(self):
        order = Review.review_objects.get(_id=1)

        name=f'{order.name}'
        rating=f'{order.rating}'
        comment=f'{order.comment}'
       
       

        self.assertEqual(name , "khaled")
        self.assertEqual(rating ,"4" )
        self.assertEqual(comment , "not bad")