from . import views
from rest_framework.routers import DefaultRouter
from django.contrib import admin

admin.site

router = DefaultRouter()

router.register("menuitems", views.MenuItemsViewSet, basename="menuitems")
router.register("articles", views.ArticleViewSet, basename="articles")
router.register("categories", views.CategoryViewSet, basename="categories")
router.register("contacts", views.ContactViewSet, basename="contacts")

urlpatterns = router.urls