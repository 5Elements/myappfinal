from django.shortcuts import render
from django.http import HttpResponse
from myapp.util.sentimental import Analyzer
from django.template import RequestContext
from myapp.models import Tweet
# Create your views here.

def index(request):
    return render(request, 'templates/myapp/index.html')

def savedData(request):
	if request.method == 'GET':
		context = RequestContext(request)
		tweet_list = Tweet.objects.all()
        # context_dict = {'tweets':tweet_list}

		return render(request, 'templates/myapp/saved.html',{'tweets':tweet_list,'total': tweet_list.count},context)

def analyzeData(request):
    if request.method == 'GET':

        req_tag = request.GET.get("tags")

        analyzer = Analyzer()
        analyzed_data = analyzer.analyzeData(req_tag)
        analyzed_data['tag'] = '#' + req_tag.upper()
        #print(analyzed_data)
        return render(request, 'templates/myapp/analysis.html', analyzed_data)