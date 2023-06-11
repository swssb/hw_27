from django.urls import path
from rest_framework import routers

from users.views import UserGenericRetrieveView, \
    UserGenericListView, UserGenericCreateView, UserGenericUpdateView, UserGenericDestroyView, LocationViewSet

router = routers.SimpleRouter()
router.register('location', LocationViewSet)
router.register('location/<int:pk>', LocationViewSet)
urlpatterns = [
    path("user/", UserGenericListView.as_view()),
    path("user/<int:pk>/", UserGenericRetrieveView.as_view()),
    path("user/create/", UserGenericCreateView.as_view()),
    path("user/<int:pk>/update/", UserGenericUpdateView.as_view()),
    path("user/<int:pk>/delete/", UserGenericDestroyView.as_view())
]

urlpatterns += router.urls