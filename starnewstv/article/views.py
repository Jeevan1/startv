from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from article.pagination import DefaultPagination
from .filters import ArticleFilter, MenuItemFilter
from utils.api_mixins import BaseAPIMixin
from article.models import Article, Author, Category, Contact, MenuItem
from article.serializers import ArticleCreateSerializer, ArticleDetailSerializer, ArticleSerializer, AuthorSerializer, CategorySerializer, ContactSerializer, MenuItemsSerializer
# Create your views here.

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import MenuItem
from .filters import MenuItemFilter

class MenuItemsViewSet( BaseAPIMixin,ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MenuItemFilter

    def list(self, request, *args, **kwargs):
        grouped_menus = {
            "header": MenuItem.objects.filter(position="header", parent=None),
            "footer": MenuItem.objects.filter(position="footer", parent=None),
            "sidebar": MenuItem.objects.filter(position="sidebar", parent=None),
        }

        response_data = {
            "header": MenuItemsSerializer(grouped_menus["header"], many=True).data,
            "footer": MenuItemsSerializer(grouped_menus["footer"], many=True).data,
            "sidebar": MenuItemsSerializer(grouped_menus["sidebar"], many=True).data,
        }

        return Response(response_data)


class CategoryViewSet(BaseAPIMixin,ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class AuthorViewSet(BaseAPIMixin,ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class ArticleViewSet(BaseAPIMixin, ModelViewSet):
    queryset = Article.objects.select_related("author", "category").all()
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter,OrderingFilter]
    filterset_class = ArticleFilter
    search_fields = ["title", "content"]
    pagination_class = DefaultPagination
    ordering_fields = ["created_at"]

    def get_serializer_class(self):
        if self.action == "list":
            return ArticleSerializer
        if self.action == "retrieve":
            return ArticleDetailSerializer
        if self.action == "create":
            return ArticleCreateSerializer
        
        return ArticleSerializer
    
class ContactViewSet(BaseAPIMixin,ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
