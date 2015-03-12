from django.contrib import admin

from reclama.sprints.models import Event, Bug, Prize


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date', 'owner', 'archived', 'url')
    list_filter = ['archived']
    readonly_fields = ('created_date',)
    change_list_template = 'admin/change_list_filter_sidebar.html'

    def url(self, obj):
        return '<a href="{0}" target="_blank">{0}</a>'.format(obj.link)

    def created_date(self, obj):
        return obj.created_at.strftime('%d.%m.%Y')

    url.allow_tags = True


class PrizeAdmin(admin.ModelAdmin):
    fields = ('name', )


class BugAdmin(admin.ModelAdmin):
    list_display = ('number', 'url')

    def url(self, obj):
        return '<a href="{0}" target="_blank">{0}</a>'.format(obj.bug_url)

    url.allow_tags = True

admin.site.register(Event, EventAdmin)
admin.site.register(Prize, PrizeAdmin)
admin.site.register(Bug, BugAdmin)
