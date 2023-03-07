from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("blogs", views.blogs, name="blogs"),
    path("bookstore", views.bookstore, name="bookstore"),
    path("library", views.library, name="library"),
    path("help", views.helps, name="help"),
    path("events", views.events, name="events"),
    path("admin-signup", views.register, name="admin-signup"),
    path("admin-page", views.adminpage, name="admin-page"),
    path("admin-login", views.login_user, name="admin-login"),
    path("logout", views.logout_user, name="logout"),
    path("post/<str:pk>", views.post, name="post")
]