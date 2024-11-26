from django.test import TestCase
from django.urls import reverse_lazy, reverse

from taxi.forms import CarSearchForm


class CreateTest(TestCase):
    def test_car_search(self):
        data = {
            "model": "F",
            "page": 1,
        }
        response = self.client.get(
            reverse_lazy("taxi:car-list"),
            data,
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "model")
        self.assertContains(response, "page")

    def test_driver_search(self):
        data = {
            "username": "A",
            "page": 1,
        }
        response = self.client.get(
            reverse_lazy("taxi:driver-list"),
            data,
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "username")
        self.assertContains(response, "page")

    def test_manufacturer_search(self):
        data = {
            "name": "T",
            "page": 1,
        }
        response = self.client.get(
            reverse_lazy("taxi:manufacturer-list"),
            data,
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "name")
        self.assertContains(response, "page")