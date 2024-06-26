from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
# from rest_framework_swagger.views import get_swagger_view
# Swagger is no longer supported and django 3.0 broke it
SchemaView= get_schema_view(title="Blog API")
DocsView= include_docs_urls(title="Blog API")
# SwaggerView= get_swagger_view(title="Blog API")

from. import views
router=SimpleRouter()
router.register("",views.PostViewSet,basename="post")
urlpatterns = [
    path("auth/", include('rest_framework.urls')),
    path("users/", views.UserList.as_view(), name="user-list"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
    path("schema/", SchemaView),
    path("docs/", DocsView),
    path("swagger-docs/", SwaggerView),
]
urlpatterns.extend(router.urls)