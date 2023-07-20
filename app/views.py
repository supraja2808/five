from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def seetha(request):
    return HttpResponse('<i><marquee><h1>i am seetha</i></marquee></h1>')


def supraja(request):
    return HttpResponse('<h1><b>hai how are you</b></h1')
