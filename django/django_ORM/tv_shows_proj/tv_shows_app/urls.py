from django.urls import path
from . import views

urlpatterns = [
    path('', views.shows),
    path('shows', views.shows),
    path('shows/new', views.add_show_page),
    path('shows/create', views.add_show),
    path('shows/<int:id>', views.display_show),
    path('shows/<int:id>/edit', views.edit_show_page),
    path('shows/<int:id>/update', views.edit_show),
    path('shows/<int:id>/destroy', views.delete_show)
]