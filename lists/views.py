from django.shortcuts import render, redirect
from django.http import HttpResponse

from lists.models import Item, List


# Create your views here.


def home_page(request):
    return render(request, "home.html", {"items": Item.objects.all()})

def new_list(request):
    if request.method == "POST":
        list = List.objects.create()
        Item.objects.create(description=request.POST['todo_text'],list=list)
        return redirect(f'/lists/{list.id}/')
def view_list(request,list_id):
    list = List.objects.get(id=list_id)
    items = Item.objects.filter(list=list)
    return render(request, "list.html", {"items": items})
