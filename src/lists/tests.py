from django.test import TestCase

from lists.models import Item, List


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
        list = List.objects.get()
        self.assertRedirects(response, f"/lists/{list.id}/")
class ListViewTest(TestCase):
    def test_renders_input_form(self):
        list = List.objects.create()
        response = self.client.get(f"/lists/{list.id}/")
        self.assertContains(response, f'<form method="POST" action="/lists/{list.id}/add">')
        self.assertContains(response, '<input name="todo_text"')

    def test_displays_all_list_items(self):
        list = List.objects.create()
        Item.objects.create(description="itemey 1",list=list)
        Item.objects.create(description="itemey 2",list=list)

        response = self.client.get(f"/lists/{list.id}/")

        self.assertContains(response, "itemey 1")
        self.assertContains(response, "itemey 2")
    def test_save_retrival_list_listitem(self):
        list = List()
        list.save()
        list_item_1 = Item.objects.create(description="item 1",list=list)
        list_item_2 = Item.objects.create(description="item 2",list=list)
        self.assertEqual(List.objects.get(), list)

        items = Item.objects.all()
        self.assertEqual(items.count(), 2)
        self.assertEqual(items[0].description, "item 1")
        self.assertEqual(items[1].description, "item 2")
        self.assertEqual(items[0].list, list)
        self.assertEqual(items[1].list, list)
class AddItemTest(TestCase):
    def test_add_item(self):
        list = List.objects.create()
        self.client.post(f"/lists/{list.id}/add", data={'todo_text': "add item"})
        new_item = Item.objects.get()
        self.assertEqual(new_item.list, list)
        self.assertEqual(new_item.description, "add item")
    def test_redirect_after_POST(self):
        correct_list = List.objects.create()
        response = self.client.post(
            f"/lists/{correct_list.id}/add",
            data={"todo_text": "A new item for an existing list"},
        )
        self.assertRedirects(response, f"/lists/{correct_list.id}/")
    def test_input_form(self):
        list = List.objects.create()
        response = self.client.get(f"/lists/{list.id}/")
        self.assertContains(response, f'<form method="POST" action="/lists/{list.id}/add">')


