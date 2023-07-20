from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rama(request):
    return HttpResponse('<h1><b>this is rama</b></h1>')
