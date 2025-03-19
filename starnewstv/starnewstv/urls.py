from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "StarNews Admin"
admin.site.site_title = "StarNews Admin Portal"
admin.site.index_title = "Welcome to StarNews Admin Portal"

urlpatterns = [
    path("api/jwt/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("admin/", admin.site.urls),
    path("", include("article.urls")),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
