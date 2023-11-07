from django.contrib import admin
from .models import Applications

@admin.register(Applications)
class PaladinAdmin(admin.ModelAdmin):
    list_display = ('name','phone','comment', 'create_time', 'status')
    ordering = ['-create_time']
    list_editable = ('status', )
    list_per_page = 10
    actions = ['setCompleted','setCanceled','setAwaiting']
    search_fields = ['name','phone','email',]


    @admin.action(description='Пометить выполненными')
    def setCompleted(self, request, queryset):
        count = queryset.update(status=Applications.Status.COMPLETED)
        self.message_user(request, f'Завершено {count} заявок.')
    @admin.action(description='Пометить отказанными')
    def setCanceled(self, request, queryset):
        count = queryset.update(status=Applications.Status.CANCELED)
        self.message_user(request, f'Отменено {count} заявок.')

    @admin.action(description='Пометить ожидающими')
    def setAwaiting(self, request, queryset):
        count = queryset.update(status=Applications.Status.AWAITING)
        self.message_user(request, f'{count} заявок в ожидании.')