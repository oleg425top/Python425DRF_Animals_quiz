from django.contrib import admin
from sections.models import Section, Content, Question
# Register your models here.

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'slug')
    list_filter = ('title',)
    ordering = ('id')
    search_fields = ('title',)

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_filter = ('section',)
    ordering = ('id', 'section')
    search_fields = ('title',)


@admin.register(Question)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'section', 'question', 'description', 'answer')
    list_filter = ('section',)
    ordering = ('id', 'section')
    search_fields = ('question',)
