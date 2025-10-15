from django.test import TestCase
from django.http import HttpRequest

from lists.models import Item
from lists.views import home_page

# Create your tests here.


class HomePageTest(TestCase):
    def test_bad_maths(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_returns_correct_html_2(self):
        response = self.client.get("/")
        self.assertContains(response, "<title>To-Do lists</title>")

    def test_todo_form(self):
        response = self.client.get("/")
        self.assertContains(response, '<form method="POST">')
        self.assertContains(response, '<input name="todo_text"')
    def test_save_todo(self):
        self.client.post("/", data={'todo_text': "buy vegetables"})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.description, 'buy vegetables.')
    def test_redirect_after_post(self):
        response = self.client.post("/", data={'todo_text': "buy vegetables"})
        self.assertRedirects(response, "/")
