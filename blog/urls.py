from django.urls import path
from . import views

urlpatterns = [
    path("", views.homePage, name="home-page"),  # for the homepage
    # for the page containing all posts
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post_details,
         name="post-detail-page")  # for individual posts
]
