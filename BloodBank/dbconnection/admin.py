from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(UserDetails)
admin.site.register(RequestDetails)
admin.site.register(BloodBankDetails)
admin.site.register(AvailableBloodGroup)


class FAQAdmin(admin.ModelAdmin):
	list_display=('question','category','enabled')
	list_filter=('category','enabled')
	search_fields=('question','answer')


admin.site.register(FAQ,FAQAdmin)