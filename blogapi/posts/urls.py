from django.urls import path, include
from. import views
urlpatterns = [
    path("", views.PostList.as_view(), name="post-list"),
    path("<int:pk>/",views.PostDetail.as_view(),name="post-detail"),
    path("auth/", include('rest_framework.urls')),
    path("users/", views.UserList.as_view(), name="user-list"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
]