from django.contrib import admin
from products.models import *
from mptt.admin import MPTTModelAdmin


class CustomMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
    mptt_indent_field = 'name'


@admin.register(Category)
class CategoryAdmin(CustomMPTTModelAdmin):
    list_display = ('name', 'parent')


admin.site.register(Product)
admin.site.register(ProductColour)
admin.site.register(ProductSize)
admin.site.register(ProductImage)
admin.site.register(ProductReview)
admin.site.register(Wishlist)
