from django.contrib import admin
from .models import Applications

@admin.register(Applications)
class PaladinAdmin(admin.ModelAdmin):
    list_display = ('name','phone','comment', 'create_time', 'status')
    ordering = ['-create_time']
    list_editable = ('status', )
