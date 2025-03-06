from django_filters.rest_framework import FilterSet
from django_filters import CharFilter

from store.models import Article

class ArticleFilter(FilterSet):
    category = CharFilter(field_name='category__name', lookup_expr='icontains')
    title = CharFilter(field_name='title', lookup_expr='icontains')
    class Meta:
        model = Article
        fields = ['title', 'category']