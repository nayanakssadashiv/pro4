from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index1(request):
    return HttpResponse("<h1>index1 of app1</h1>")
def rend_app1(request):
    return render(request,"app1/home1.html")