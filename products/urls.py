from django.urls import path
from . import views

# Note all URL in this app start is /products
# /products
urlpatterns = [
    path('', views.index),
    path('new', views.new)
]