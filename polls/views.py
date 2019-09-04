from django.http import HttpResponse
from django.shortcuts import render
import json


from django.http import HttpResponse


def index(request):
    return HttpResponse("You're at the infractions index.")

# Create your views here.
def detail(request, infraction):
    return HttpResponse("You're looking at infraction %s." % infraction)
