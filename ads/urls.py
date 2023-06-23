from django.urls import path

from ads.views import CategoryListView, CategoryUpdateView, AdUpdateView, \
    CategoryDeleteView, AdDeleteView, AdCreateView, CategoryCreateView, AdImageView, AdSearchView, AdRetrieveView, \
    SelectionCreateView, SelectionListView, SelectionRetrieveView, SelectionUpdateView, SelectionDeleteView, \
    CategoryRetrieveView

urlpatterns = [
    path("cat/", CategoryListView.as_view()),
    path("cat/create/", CategoryCreateView.as_view()),
    path("cat/<int:pk>/", CategoryRetrieveView.as_view()),
    path("cat/<int:pk>/update/", CategoryUpdateView.as_view()),
    path("cat/<int:pk>/delete/", CategoryDeleteView.as_view()),


    path("ad/", AdSearchView.as_view()),
    path("ad/create/", AdCreateView.as_view()),
    path("ad/<int:pk>/", AdRetrieveView.as_view()),
    path("ad/<int:pk>/update/", AdUpdateView.as_view()),
    path("ad/<int:pk>/delete/", AdDeleteView.as_view()),
    path("ad/<int:pk>/upload_image/", AdImageView.as_view()),

    path("selection/create/", SelectionCreateView.as_view()),
    path("selection/", SelectionListView.as_view()),
    path("selection/<int:pk>/", SelectionRetrieveView.as_view()),
    path("selection/<int:pk>/update/", SelectionUpdateView.as_view()),
    path("selection/<int:pk>/delete/", SelectionDeleteView.as_view()),
]
