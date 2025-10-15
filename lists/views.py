from django.shortcuts import render, redirect
from django.http import HttpResponse

from lists.models import Item


# Create your views here.


def home_page(req):
    if req.method == "POST":
        Item.objects.create(description=req.POST['todo_text'])
        return redirect('/')
    #     return HttpResponse(req.POST["todo_text"])
    return render(req, "home.html", {"items": Item.objects.all()})
