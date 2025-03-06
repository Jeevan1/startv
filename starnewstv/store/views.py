from re import search
from rest_framework.viewsets import ModelViewSet

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import ArticleFilter
from utils.api_mixins import BaseAPIMixin
from store.models import Article, Category, Contact, MenuItems
from store.serializers import ArticleCreateSerializer, ArticleDetailSerializer, ArticleSerializer, CategorySerializer, ContactSerializer, MenuItemsSerializer
# Create your views here.

class MenuItemsViewSet(BaseAPIMixin,ModelViewSet):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializer

class CategoryViewSet(BaseAPIMixin,ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ArticleViewSet(BaseAPIMixin, ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ArticleFilter
    search_fields = ["title", "content"]

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

