from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic

# def index(request):
    # latest_question_list = Question.objects.order_by('pub_date')[:5:]
    # #222 template = loader.get_template('pools/index.html') # 获取HTML 的jinjia2页面
    # #111  output = ','.join([str(q.question_text)+'|||'  for q in latest_question_list])
    # context={
	    # 'latest_question_list':latest_question_list
		# }
    # #222  return HttpResponse(template.render(context, request))  # render 渲染整合模板和数据
    # #111  return HttpResponse(output)
    # return render(request, 'pools/index.html', context)


###########  MY VIEW #################################################
def myhtml5():
    return r"""
<html>
<body>
<h1>This is heading 1 </h1>
</body>
</html>
"""

def sogood(request):
    return HttpResponse(myhtml5())
	
def getid(request, id):
    return HttpResponse("get id:%s" %id)

##############################################################################
# def detail(request, question_id):
    # #try:
	# #    print(help(Question.objects.get))
	# #    question = Question.objects.get(pk=question_id)
    # #except Question.DoesNotExist:
    # #    raise Http404("Question dose not exist !")
    # #return render(request, 'pools/detail.html', {'question':question})
    # #return HttpResponse("You're looking at question %s." % question_id)
	
	# question = get_object_or_404(Question, pk=question_id)
	# return render(request, 'pools/detail.html', {'question':question})

	
# def results(request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'pools/results.html', {'question': question})
	
	
# def results(request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    # print(question.question_text)
    # #response = "You're looking at the results of question %s."
    # #return HttpResponse(response % question_id)
    # return render(request, 'pools/results.html', {'question':question})

def vote(request, question_id):
    #return HttpResponse("You're voting on question %s." % question_id)
	#def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'pools/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('pools:results', args=(question.id,)))
	
class IndexView(generic.ListView):
    template_name = 'pools/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'pools/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'pools/results.html'
	
	
	