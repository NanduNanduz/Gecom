from django.shortcuts import render
from django.http import HttpResponse 
from django.views.generic import (
                                ListView
)
# Create your views here.

def component(request):
    return HttpResponse("this is component")