"""
__author__ = "Andre Litty"
__copyright__ = "Copyright 2018"
__license__ = "GPL"
__email__ = "alittysw@gmail.com"
"""
from django.urls import include, path, re_path
from rest_framework import routers, permissions
from rest_framework.schemas import get_schema_view, openapi

from boards.views import ListViewSet

from django.urls import path, include, re_path
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Router provides routes for standard CRUD functionality
router = routers.DefaultRouter()
router.register(r'', ListViewSet, basename='list')

urlpatterns = [
    path('lists/', include(router.urls)),
]
schema_view = get_schema_view(
    openapi.Info(
        title="Board Management API",
        default_version='v1',
        description="API for managing boards, lists, and labels.",
        terms_of_service="https://example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# URL patterns
urlpatterns = [
    path('api/', include(router.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]