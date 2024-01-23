from django.urls import path
from . import views

urlpatterns = [
    path('apostilas/', views.apostilas, name='apostilas')
]
