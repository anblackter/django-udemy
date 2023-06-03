from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("january", views.january),
    path("february", views.february)
]
