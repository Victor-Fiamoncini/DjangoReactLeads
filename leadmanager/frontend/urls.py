# Imports
from django.urls import path
from . import views

# Urls
urlpatterns = [
  path('', views.index)
]
