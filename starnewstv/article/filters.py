from django_filters.rest_framework import FilterSet
from django_filters import CharFilter

from article.models import Article, MenuItem

class MenuItemFilter(FilterSet):
    label = CharFilter(field_name='label', lookup_expr='iexact')
    parent = CharFilter(field_name='parent', lookup_expr='iexact')
    position = CharFilter(field_name='position', lookup_expr='iexact')

    class Meta:
        model = MenuItem
        fields = ['label', 'parent', 'position']

class ArticleFilter(FilterSet):
    category = CharFilter(field_name='category__name', lookup_expr='iexact')
    category_idx = CharFilter(field_name='category__idx', lookup_expr='iexact')
    title = CharFilter(field_name='title', lookup_expr='icontains')
    author = CharFilter(field_name='author__user__username', lookup_expr='iexact')
    author_idx = CharFilter(field_name='author__idx', lookup_expr='iexact')
    class Meta:
        model = Article
        fields = ['title', 'category', 'author', 'category_idx', 'author_idx']