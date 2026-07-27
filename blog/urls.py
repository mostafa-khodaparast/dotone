from django.urls import path
from blog.views import test

urlpatterns = [
    path("blog/", test),
]
