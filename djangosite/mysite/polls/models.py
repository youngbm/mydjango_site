from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
import datetime

@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
	
    def __str__(self):
	    return self.question_text
		
    def was_published_recently(self):
        now = timezone.now()
        print(now - datetime.timedelta(days=1))
        #return now - datetime.timedelta(days=1) <= self.pub_date < = timezone.now()
        return  timezone.now() - datetime.timedelta(days=2) <= self.pub_date <= timezone.now()
        
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
        
@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
	
    def __str__(self):
        return self.choice_text