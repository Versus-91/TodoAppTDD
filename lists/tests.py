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
        self.assertContains(response, '<form method="POST"')
        self.assertContains(response, '<input name="todo_text"')

    def test_save_todo(self):
        self.client.post("/lists/new", data={'todo_text': "buy vegetables"})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.description, 'buy vegetables')
    def test_redirects_after_POST(self):
        response = self.client.post("/lists/new", data={"todo_text": "test todo item"})
        self.assertRedirects(response, "/lists/unique-list/")
class ListViewTest(TestCase):
    def test_renders_input_form(self):
        response = self.client.get("/lists/unique-list/")
        self.assertContains(response, '<form method="POST" action="/">')
        self.assertContains(response, '<input name="todo_text"')

    def test_displays_all_list_items(self):
        Item.objects.create(description="itemey 1")
        Item.objects.create(description="itemey 2")

        response = self.client.get("/lists/unique-list/")

        self.assertContains(response, "itemey 1")
        self.assertContains(response, "itemey 2")
