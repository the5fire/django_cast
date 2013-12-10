#coding:utf-8

from django.shortcuts import render

from .models import Cast
# Create your views here.


def index(request):
    casts = Cast.objects.all()
    return render(request, "index.html", {"casts": casts})
