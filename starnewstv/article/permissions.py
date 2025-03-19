from rest_framework import permissions
from rest_framework.permissions import BasePermission

from rest_framework import permissions

from article.models import Article, Author

class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author.user == request.user

class IsAdminOrAuthor(BasePermission):
    def has_permission(self, request, view):
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if isinstance(obj, Author):
            return obj.user == request.user or request.user.is_superuser
        
        if isinstance(obj, Article):
            return obj.author.user == request.user or request.user.is_superuser


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser
