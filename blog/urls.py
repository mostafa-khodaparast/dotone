from django.urls import path
from blog.views import post_list, post_detail

urlpatterns = [
    path("list/", post_list),
    path("post_detail/<int:post_id>/", post_detail),
]
