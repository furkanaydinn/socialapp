from django.contrib import admin
from .models import User, FriendshipRequest

class FriendshipRequestAdmin(admin.ModelAdmin):
    list_display = ('created_for', 'created_by', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('created_for__email', 'created_by__email', 'created_for__name', 'created_by__name')
    list_editable = ('status',)
    actions = ['accept_requests', 'reject_requests']

    def accept_requests(self, request, queryset):
        queryset.update(status=FriendshipRequest.ACCEPTED)

    accept_requests.short_description = "Accept selected friendship requests"

    def reject_requests(self, request, queryset):
        queryset.update(status=FriendshipRequest.REJECTED)

    reject_requests.short_description = "Reject selected friendship requests"


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'is_active', 'is_staff', 'is_superuser', 'date_joined')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'name')
    list_editable = ('is_active', 'is_staff', 'is_superuser')
    actions = ['activate_users', 'deactivate_users']

    def activate_users(self, request, queryset):
        queryset.update(is_active=True)

    activate_users.short_description = "Activate selected users"

    def deactivate_users(self, request, queryset):
        queryset.update(is_active=False)

    deactivate_users.short_description = "Deactivate selected users"


admin.site.register(FriendshipRequest, FriendshipRequestAdmin)
admin.site.register(User, UserAdmin)

