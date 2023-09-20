from django.urls import path
from pages import views

urlpatterns = [
    path("about/", views.AboutMe,name="about"),
]