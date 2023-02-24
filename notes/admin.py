from django.contrib import admin
from django.db.models.aggregates import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models

# Register your models here.

@admin.register(models.Author)
class AthorAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'first_name', 'last_name',  'tier', 'notes']
    list_editable = ['tier']
    list_per_page = 10
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']

    @admin.display(ordering='notes_count')
    def notes(self, author):
        url = (
            reverse('admin:notes_note_changelist')
            + '?'
            + urlencode({
                'author__id': str(author.id)
            }))
        return format_html('<a href="{}">{} Notes</a>', url, author.notes_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            notes_count=Count('notes')
        )



@admin.register(models.Note)
class NoteAdmin(admin.ModelAdmin):
    autocomplete_fields = ['author']
    list_display = ['id', 'created', 'author']
