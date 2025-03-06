from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "StarNews Admin"
admin.site.site_title = "StarNews Admin Portal"
admin.site.index_title = "Welcome to StarNews Admin Portal"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("store.urls")),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
