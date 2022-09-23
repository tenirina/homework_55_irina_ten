from django.contrib import admin

from webapp.models import ToDo


class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'status', 'completion_data')
    list_filter = ('id', 'text', 'status', 'completion_data')
    search_fields = ('text', 'status', 'completion_data')
    fields = ('id', 'text', 'status', 'completion_data')
    readonly_fields = ('id', 'text')


admin.site.register(ToDo, ToDoAdmin)
