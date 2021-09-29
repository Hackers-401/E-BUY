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
