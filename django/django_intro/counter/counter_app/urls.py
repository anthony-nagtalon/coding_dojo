from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add', views.add),
    path('double', views.double),
    path('destroy_session', views.destroy_session)
]