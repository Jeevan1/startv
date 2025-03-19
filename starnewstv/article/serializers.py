from dataclasses import fields
from rest_framework import serializers

from utils.serializers_mixins import BaseModelSerializer
from article.models import Article, Author, Category, Contact, MenuItem

class MenuItemsSerializer(BaseModelSerializer):
    children = serializers.SerializerMethodField()
    class Meta:
        model = MenuItem
        fields = ["position", "parent","label", "url", "children"]
    
    def get_children(self, obj):
        children = obj.children.all()
        return MenuItemsSerializer(children, many=True).data

class CategorySerializer(BaseModelSerializer):
    class Meta:
        model = Category
        fields = ["idx", "name"]

class AuthorSerializer(BaseModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Author
        fields = ["idx", "name", "user", "phone", "image"]

    def get_user(self, obj):
        return obj.user.username

class ArticleSerializer(BaseModelSerializer):
    category = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()
    class Meta:
        model = Article
        fields = ["idx", "title", "category", "content","author", "featured_image","created_at"]

    def get_category(self, obj):
        return obj.category.name

    def get_author(self, obj):
        return obj.author.name
    

class ArticleDetailSerializer(ArticleSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Article
        fields = ["idx", "title", "content", "category","author","created_at", "featured_image"]


class ArticleCreateSerializer(BaseModelSerializer):
    class Meta:
        model = Article
        fields = ["idx", "title", "content","author", "category", "featured_image"]
    
class ContactSerializer(BaseModelSerializer):
    class Meta:
        model = Contact
        fields = ["idx", "name", "email", "subject", "phone", "message"]