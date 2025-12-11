# core/views.py
from django.http import HttpResponse
from django.shortcuts import render


def docs(request):
    return render(request, "core/docs.html")


def index(request):
    return render(request, "core/index.html")
