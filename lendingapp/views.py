from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import models

# Create your views here.
def index(request):    
    return render(request, 'index.html')

def status(request):
    costumes = models.Item.objects.all()
    return render(request, 'status.html', {'costumes': costumes})
    # return render(request, 'empty.html', {'costumes': costumes})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

