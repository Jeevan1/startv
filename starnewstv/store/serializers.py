from dataclasses import fields
from rest_framework import serializers

from utils.serializers_mixins import BaseModelSerializer
from store.models import Article, Category, Contact, MenuItems

class MenuItemsSerializer(BaseModelSerializer):
   
    class Meta:
        model = MenuItems
        fields = ["idx", "label", "url", "parent", "position"]

class CategorySerializer(BaseModelSerializer):
    class Meta:
        model = Category
        fields = ["idx", "name"]

class ArticleSerializer(BaseModelSerializer):
    class Meta:
        model = Article
        fields = ["idx", "title", "category", "featured_image"]

class ArticleDetailSerializer(ArticleSerializer):
    class Meta:
        model = Article
        fields = ["idx", "title", "content", "category", "featured_image"]

class ArticleCreateSerializer(BaseModelSerializer):
    class Meta:
        model = Article
        fields = ["idx", "title", "content", "category", "featured_image"]
    
class ContactSerializer(BaseModelSerializer):
    class Meta:
        model = Contact
        fields = ["idx", "name", "email", "subject", "phone", "message"]