from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Create your views here.
def hello(request):
    s = request.GET.get('s', '')
    return HttpResponse(f'Hello, {s} world!')