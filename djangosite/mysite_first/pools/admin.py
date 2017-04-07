from django.contrib import admin
from .models import Question, Choice
# Register your models here.

# admin.site.register(Question)
#admin.site.register(Choice)

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("问题内容：",       {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)