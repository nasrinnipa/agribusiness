from django.shortcuts import render
from django.http import HttpResponse

def seller(request):
    return HttpResponse("Seller ")