from django.urls import path, include
from. import views
urlpatterns = [
    path("", views.PostList.as_view(), name="postlist"),
    path("<int:pk>/",views.PostDetail.as_view()),
    path("auth/", include('rest_framework.urls'),)
]