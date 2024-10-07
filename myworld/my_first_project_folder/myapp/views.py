from django.shortcuts import render
from django.http import HttpResponse

def myapp(request):
    return render( request, "index.html")
def index(request):
    return render( request, "index.html")




def contract(request):
    return render( request, "contract.html")

def about(request):
    return render( request, "about.html")

def agroff(request):
    return render( request, "agroff.html")

def chem(request):
    return render( request, "chem.html")

def dashboard(request):
    return render( request, "dashboard.html")

def farm(request):
    return render( request, "farm.html")
def harv(request):
    return render( request, "harv.html")

def farmerssignup(request):
    return render( request, "farmerssignup.html")


def login(request):
    return render( request, "login.html")

def market(request):
    return render( request, "market.html")

def prod(request):
    return render( request, "prod.html")

def prof(request):
    return render( request, "prof.html")
def signup(request):
    return render( request, "signup.html")

def start(request):
    return render( request, "start.html")

def admin(request):
    return render( request, "admin.html")