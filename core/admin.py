from django.contrib import admin
from core.models import Provider
# Register your models here.


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)
    # ordering = ['created']
    fieldsets = (
        (None, {
            'fields': ('name', 'email')
        }),
    )
