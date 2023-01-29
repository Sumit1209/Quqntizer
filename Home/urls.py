from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('', views.home,name='Home'),
    path('about', views.about ,name='about'),
    path('contact', views.contact,name='contact'),
    path('services', views.services,name='services'),
    path('feed', views.feedback, name='feedback'),

    path("search",views.search, name="search"),
    path('Detail/<ilabel>',views.Detailpage),
    path('Details/<ilabel>',views.Detailpage2),
    path('Detailse/<ilabel>',views.Detailpage3),



]