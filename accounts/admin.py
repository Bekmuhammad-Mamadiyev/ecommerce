from django.contrib import admin
from accounts.models import *
from django.contrib.auth.models import Group

admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'phone_number', 'address')


@admin.register(VerificationOtp)
class VerificationOtpAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'code', 'type', 'expires_in')

@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'name', 'phone_number', 'apartment','street', 'pin_code')
