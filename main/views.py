from django.shortcuts import render, render_to_response
from django.template import RequestContext


def home_view(request):

    context = {}

    return render_to_response('home_view.html', context, context_instance=RequestContext(request))
