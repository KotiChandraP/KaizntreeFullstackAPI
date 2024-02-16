from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Item

def test_get_item_list(self):
    response = self.client.get('/items/')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)

def test_filter_items_by_category(self):
    response = self.client.get('/items/?category=' + str(category.id))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)

def test_filter_items_by_stock_status(self):
    response = self.client.get('/items/?stock_status=' + Item.StockStatus.IN_STOCK.value)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)

def test_invalid_filter_parameter(self):
    response = self.client.get('/items/?invalid_param=Test')
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    


