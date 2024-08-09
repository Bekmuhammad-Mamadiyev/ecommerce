from django.contrib import admin
from products.models import *



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')


admin.site.register(Product)
admin.site.register(ProductColour)
admin.site.register(ProductSize)
admin.site.register(ProductImage)
admin.site.register(ProductReview)
admin.site.register(Wishlist)
