from django.conf.urls import url
from . import views


app_name='pools'
urlpatterns = [
    # url(r'^hello$', views.index, name='index'),
	# url(r'^goods$', views.sogood, name='sogood'),
	# url(r'^getid_(?P<id>[\w]+)$', views.getid, name='getid'),
    # # ex: /pools/5/
    # url(r'^(?P<question_id>[0-9]+)/detail$', views.detail, name='detail'),
    # # ex: /pools/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /pools/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]