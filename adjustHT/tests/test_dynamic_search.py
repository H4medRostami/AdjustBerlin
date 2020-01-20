from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from adjustHT.models import Dataset
import json
class AdjustHTAppTest(APITestCase):

    def setUp(self):
        # search reverse urls:
        self.read_url = reverse('Filter_Dataset-list')

        """ dynamic search
            Method : GET
            Permission : AllowAny
            Authentication : anybody
        """
        self.data = Dataset.objects.create(country='IR', os='ios', revenue=20, impressions=1500, installs=2,
                                           clicks=1002, channel='fokTV', spend=125, date='2017-06-01')
        self.data.save()

    def test_search(self):
        response = self.client.get(self.read_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        response = self.client.get(self.read_url+'?sort_by=-clicks&country=ir')
        data = response.json()
        for i in data:
            print(i)
            self.assertEquals(i['country'], 'IR')
