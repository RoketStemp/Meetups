from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:slug>/success', views.confirm_registration, name='confirm-registration'),
    path('<str:slug>/', views.meetup_detail, name='meetup-detail')
]