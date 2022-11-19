from django.urls import path
from . import views
urlpatterns = [
    path("product/", views.product, name="product"),
    path("topic/", views.topic, name="topic"),
]
