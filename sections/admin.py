from django.contrib import admin
from sections.models import Section, Content, Question


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_filter = ('title',)
    ordering = ('id',)
    search_fields = ('title',)

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'section')
    list_filter = ('section',)
    ordering = ('id', 'section')
    search_fields = ('title',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'section', 'question', 'description', 'answer')
    list_filter = ('section',)
    ordering = ('id', 'section')
    search_fields = ('answer',)
