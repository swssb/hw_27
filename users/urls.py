from django.urls import path

from users.views import UserListView, UserDetailView, UserUpdateView, UserDeleteView, \
    UserGenericCreateView

urlpatterns = [
    path("user/", UserListView.as_view()),
    path("user/<int:pk>/", UserDetailView.as_view()),
    path("user/create/", UserGenericCreateView.as_view()),
    path("user/<int:pk>/update/", UserUpdateView.as_view()),
    path("user/<int:pk>/delete/", UserDeleteView.as_view())
]