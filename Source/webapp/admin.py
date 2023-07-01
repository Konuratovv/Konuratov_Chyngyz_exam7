from django.contrib import admin

from webapp.models import GuestBook


class GuestBookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'email', 'status', 'created_at']
    list_display_links = ['id', 'title']
    list_filter = ['status']
    search_fields = ['title', 'text', 'email']
    fields = ['title', 'email', 'text', 'status']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(GuestBook, GuestBookAdmin)
