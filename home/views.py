from django.http import HttpResponse
# from django.shortcuts import render


def home(request):
    print('Home')
    return HttpResponse('Home from app')
