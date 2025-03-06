from django.contrib import admin

from store.models import Article, Category, MenuItems

# Register your models here.

class MenuItemsAdmin(admin.ModelAdmin):
    list_display = ('label', 'url', 'parent')

admin.site.register(MenuItems, MenuItemsAdmin)
admin.site.register([Category])
admin.site.register([Article])