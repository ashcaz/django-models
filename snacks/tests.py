from django.test import TestCase
from django.urls import reverse


class SnacksTest(TestCase):
    def test_home_page_status(self):
        url = reverse("snacks_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        url = reverse("snacks_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snacks_list.html")

    def test_base_page_template(self):
        url = reverse("snacks_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "base.html")
