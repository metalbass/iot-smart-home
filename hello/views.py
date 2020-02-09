from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


def api(request):
    print("API got called\n\nstr:" + str(request))

    return HttpResponse("{}")

def auth(request):
    print("auth got called\n\nstr:" + str(request))

    return HttpResponse("{}")

def token(request):
    print("token got called\n\nstr:" + str(request))

    return HttpResponse("{}")

