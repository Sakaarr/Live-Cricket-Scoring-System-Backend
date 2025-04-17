from django.contrib import admin
from .models import *

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Match)
admin.site.register(Inning)
admin.site.register(Ball)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'logo_preview')
    readonly_fields = ('logo_preview',)

    def logo_preview(self, obj):
        if obj.logo:
            return mark_safe(f'<img src="{obj.logo.url}" width="100" />')
        return "No logo"
    logo_preview.short_description = 'Logo Preview'

