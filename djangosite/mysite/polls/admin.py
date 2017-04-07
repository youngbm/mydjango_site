from django.contrib import admin
from .models import Question, Choice
# Register your models here.


#class ChoiceInline(admin.StackedInline): # 竖着
class ChoiceInline(admin.TabularInline): #横着
    model = Choice
    extre = 3



class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']  
    fieldsets = [
        ('Question Info',          {'fields':['question_text']}),
        ('Date Info' ,   {'classes':['collaspse'], 'fields':['pub_date'] }),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    
admin.site.register(Question, QuestionAdmin)