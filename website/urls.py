from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
path('',views.home,name='home'),
path('upayland',views.upayland,name='upayland'),
path('whitepaper',views.whitepaper,name='whitepaper'),
path('team',views.team,name='team'),
path('metaverse/', views.metaverse, name='metaverse'),
path('nft/', views.nft, name='nft'),
]
