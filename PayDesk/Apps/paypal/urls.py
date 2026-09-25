from django.urls import path
from . import views

app_name = 'paypal'

urlpatterns = [
    path('settings/', views.settings, name='settings'),
]