from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from account.models import Account


@admin.register(Account)
class AccountAdmin(UserAdmin):
    def fullName(self, obj):
        return obj.first_name + " " + obj.last_name

    list_display = ['fullName','email', 'username', 'is_admin', 'is_staff', 'is_superuser', 'last_login']
    list_filter = ['is_admin', 'is_staff', 'is_superuser']
    search_fields = ['fullName','email', 'username', 'is_admin', 'is_staff', 'is_superuser', 'last_login']
    readonly_fields = ['last_login', 'date_joined']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
