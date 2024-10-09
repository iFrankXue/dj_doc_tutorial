from typing import Any
from django.contrib import admin
from django.http import HttpRequest

from .models import Question, Choice

# Register your models here.

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ["pub_date", "question_text"]

# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3

class ChoiceInline(admin.TabularInline):
    model = Choice
    # extra = 3
    def get_extra(self, request, obj = None , **kwargs):
        if obj:
            return 0
        return 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

    list_per_page = 2
    date_hierarchy = "pub_date"
    ordering = ['pub_date']

admin.site.register(Question, QuestionAdmin)
admin.site.site_header = "Poll Administrator in Admin"
admin.site.site_title = "My Poll Admin Site"
admin.site.index_title = "My Poll Admin IndexPage"

# admin.site.register(Question)
# admin.site.register(Choice)