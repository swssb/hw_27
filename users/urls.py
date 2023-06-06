from django.urls import path

from users.views import UserListView, UserDetailView, UserCreateView, UserUpdateView

urlpatterns = [
    path("user/", UserListView.as_view()),
    path("user/<int:pk>/", UserDetailView.as_view()),
    path("user/create/", UserCreateView.as_view()),
    path("user/<int:pk>/update/", UserUpdateView.as_view())
]