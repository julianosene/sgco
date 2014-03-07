from django.shortcuts import render


from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader, Context

from django.contrib.auth.forms import AuthenticationForm

def home(request):
    next = request.GET.get('next', None)
    if request.user.is_authenticated():
            return(redirect("admin:index"))            
    else:
        form = AuthenticationForm()
        return render_to_response('registration/login.html', locals(), context_instance=RequestContext(request),)

    
