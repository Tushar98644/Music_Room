from django.shortcuts import render
from django.http import HttpResponse as Httprs

# Create your views here.

def tushar(request):
    return Httprs("<h1>Hello Tushar</h1>")