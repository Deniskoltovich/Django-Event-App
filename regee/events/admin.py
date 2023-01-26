from django.contrib import admin
from .models import Event
from django.utils.safestring import mark_safe

class AttendeesInLine(admin.TabularInline):
    model = Event.attendees.through

@admin.action(description='Print events count')
def print_events_count(modeladmin, request, queryset):
    print('Events count = ', queryset.count())
     
     
@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
    list_display = ('name', 'location', 'datetime', 'organizer', 'preview')
    search_fields = ('name', 'location',)
    readonly_fields = ('preview',)
    inlines = (AttendeesInLine,)
    actions = [print_events_count]
    
    def preview(self, obj):
        if not obj.poster:
            return 'unknown'
        
        return mark_safe(f"""
                         <img src="{obj.poster.url}" height="50"
                         """)
     
     
