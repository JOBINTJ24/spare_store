from django.http import HttpResponse
from django.shortcuts import render
from .models import product

# Create your views here.
def Home(request):
    obj=product.objects.all()
    return render(request,"index.html",{'result':obj})