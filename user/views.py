from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import RequestContext
from django.shortcuts import render_to_response

# Create your views here.

admin = 'administrator'


def index(request):
    if request.user.is_authenticated():
        return Http404


def logout(request):
    if request.user.is_authenticated():
        auth.logout(request)
    return HttpResponseRedirect('/accounts/login/')


def success(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/')
    username = request.user.get_username()
    return render_to_response('success.html', context_instance=RequestContext(request))


def login(request):
    if request.user.is_authenticated():
        if request.user.get_username() == admin:
            return HttpResponseRedirect('/manage/')
        return HttpResponseRedirect('/')
    return auth.views.login(request)


def profile(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    return HttpResponseRedirect('/accounts/login/')


def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = auth.forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            auth.login(request, user=authenticate(username=form.cleaned_data['username'],
                                                  password=form.cleaned_data['password1']))
            return HttpResponseRedirect('/manage/')
    else:
        form = auth.forms.UserCreationForm()
    return render_to_response('registration/register.html', {
        'form': form,
    }, context_instance=RequestContext(request))
