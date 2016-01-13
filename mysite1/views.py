from django.http import HttpResponse,Http404
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_time(request):
    now = datetime.datetime.now()
    #t = get_template('mytemplate.html')
    #html = t.render(Context({'current_time':now}))
    #return HttpResponse(html)
    return render_to_response('mytemplate.html',{'current_time':now})

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><title>LYF</title><body>In %s hours , it will be %s.</body></html>"%(offset,dt)
    return HttpResponse(html)
