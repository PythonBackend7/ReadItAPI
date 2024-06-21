from django.contrib import admin
from .models import Contact, ContactInfo


# Register your models here.

class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'email')
    list_display_links = ('id', 'phone', 'email')
    search_fields = ('phone', 'email')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')
    list_display_links = ('id', 'name', 'email', 'phone')
    search_fields = ('name', 'email')


admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactInfo, ContactInfoAdmin)
