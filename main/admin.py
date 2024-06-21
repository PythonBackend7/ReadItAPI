from django.contrib import admin
from .models import *


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category')
    list_display_links = ('id', 'title', 'author', 'category')
    search_fields = ('title', 'author', 'category')
    filter_horizontal = ('tags',)


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Extra_info)
admin.site.register(About)
admin.site.register(HappyClients)
admin.site.register(Comment)
