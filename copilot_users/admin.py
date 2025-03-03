from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'created_at', 'updated_at')
    search_fields = ('firstname', 'lastname')