from django.urls import path, include
from rest_framework.routers import SimpleRouter

from. import views
router=SimpleRouter()
router.register("",views.PostViewSet,basename="post")
urlpatterns = [
    path("auth/", include('rest_framework.urls')),
    path("users/", views.UserList.as_view(), name="user-list"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
]
urlpatterns.extend(router.urls)