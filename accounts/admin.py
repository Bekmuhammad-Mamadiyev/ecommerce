from django.contrib import admin
from accounts.models import *
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("email", "email", "first_name", "last_name", "is_active",'is_superuser')
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ('email',"first_name", "last_name", "email")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", 'phone_number', 'address')}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    # "groups",
                    # "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )


@admin.register(VerifictionOtp)
class VerificationOtpAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'code', 'type', 'expires_in')


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'phone_number', 'apartment', 'street', 'pin_code')
