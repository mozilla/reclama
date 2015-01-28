from django.contrib import admin

from reclama.sprints.models import Event, Bug, Prize


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'owner', 'archived')
    list_filter = ['archived']


class PrizeAdmin(admin.ModelAdmin):
    fields = ('name', )


class BugAdmin(admin.ModelAdmin):
    list_display = ('number', )


admin.site.register(Event, EventAdmin)
admin.site.register(Prize, PrizeAdmin)
admin.site.register(Bug, BugAdmin)
