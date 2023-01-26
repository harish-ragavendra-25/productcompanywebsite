from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"myapp/home.html")
def products(request):
    return render(request,"myapp/products.html")
def people(request):
    return render(request,"myapp/people.html")
def contactus(request):
    return render(request,"myapp/contactus.html")