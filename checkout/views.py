from django.shortcuts import render
from django.http import HttpResponse


def sample_view(request):
    ''' sample view '''
    return HttpResponse('<h1>checkout Home</h1>')

