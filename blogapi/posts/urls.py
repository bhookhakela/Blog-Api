from django.urls import path, include
from. import views
urlpatterns = [
    path("", views.PostList.as_view(), name="post-list"),
    path("<int:pk>/",views.PostDetail.as_view(),name="post-detail"),
    path("auth/", include('rest_framework.urls'),)
]