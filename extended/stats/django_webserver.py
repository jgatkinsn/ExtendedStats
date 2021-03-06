from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

def redirect(url):
    return HttpResponseRedirect(url)

def response(*args, **kwargs):
    return HttpResponse(*args, **kwargs)

def render(template, context, request, *args, **kwargs):
    return render_to_response(template, context, context_instance=RequestContext(request), *args, **kwargs)

def csrf(request):
    import django.core.context_processors
    return django.core.context_processors.csrf(request)

def get_cookie(request, cookieName):
    return request.COOKIES.get(cookieName)