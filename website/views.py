from nis import cat
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout

from .models import *
from .forms import *
from urllib.parse import urlencode
from django.contrib import messages

from django.http import JsonResponse
from django.template.loader import render_to_string
##############################################################

def home(request):
    context = {}
    return render(request,"front_end/home/index.html",context)
def upayland(request):
    context = {}
    return render(request,"front_end/home/upayland.html",context)
def whitepaper(request):
    context = {}
    return render(request,"front_end/home/whitepaper.html",context)
def team(request):
    context = {}
    return render(request,"front_end/home/team.html",context)
def metaverse(request):
    context = {}
    return render(request,"front_end/home/metaverse.html",context)
def nft(request):
    context = {}
    return render(request,"front_end/home/nft.html",context)
