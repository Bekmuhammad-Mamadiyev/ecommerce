from django.contrib import admin

from common.models import *

admin.site.register(Media)
admin.site.register(Settings)
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(OurInstagramStory)


class CustomerFeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'customer_position', 'rank']
    search_fields = ['customer_name', 'customer_position']
    list_filter = ['rank']

    def has_add_permission(self, request):
        return False


admin.site.register(CustomerFeedback, CustomerFeedbackAdmin)
