from django.shortcuts import render
from django.http import HttpResponse
def leo(request):
    return HttpResponse('LIGY')

# Create your views here.
def index(request):
    return render(request,"index.html")