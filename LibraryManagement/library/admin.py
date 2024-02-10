from django.contrib import admin
from .models import User, Notification
from django.utils.html import format_html
from django.urls import reverse
class UserAdmin(admin.ModelAdmin):
    list_display = ["usertype", "email", "username", "is_active", "approve"]
    @admin.display(description="Approve")
    def approve(self, obj):
        if not obj.is_active:
            return format_html(
                '<a class="button" href="{}">Approve</a>',
                reverse('library-verify', args=[obj.username]), 
            )
admin.site.register(User,UserAdmin)
admin.site.register(Notification)


