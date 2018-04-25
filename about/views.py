from django.shortcuts import render
from django.http import HttpResponse

def aboutme(request):
    return HttpResponse("<h2>About me </h2>")
