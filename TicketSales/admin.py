from django.contrib import admin
from .models import Concert, Location, Time

# Register your models here.
@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ['concert', 'location', 'start_date_time', 'seat', 'status']
    search_fields = ('concert', 'location', 'status')

admin.site.register(Concert)
admin.site.register(Location)


