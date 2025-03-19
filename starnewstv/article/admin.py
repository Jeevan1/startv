from django.contrib import admin

from article.models import Article, Author, Category, MenuItem

# Register your models here.

class MenuItemsAdmin(admin.ModelAdmin):
    list_display = ('label', 'url', 'parent')

admin.site.register(MenuItem, MenuItemsAdmin)
admin.site.register([Author])
admin.site.register([Category])
admin.site.register([Article])
