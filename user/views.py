from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth import forms
from django.contrib.auth import views
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import RequestContext
from django.shortcuts import render_to_response

from user.models import User

# Create your views here.

admin = 'administrator'


def restore(request):
    return Http404


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
    return views.login(request, template_name='accounts/login.html')


def profile(request, user_id):
    user = User.objects.get(id=user_id)
    if not user:
        return Http404
    editable = False
    if request.user.is_authenticated():
        editable = (request.user.get_username() == str(user.username))
    return render_to_response(
        'accounts/profile.html',
        {
            'user': user.get_user(),
            'editable': editable
        }
    )


def profile_edit(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    user = User.objects.filter(username=request.user.get_username())
    if request.method == 'GET':
        return render_to_response(
            'accounts/profile_edit.html',
            {
                'user': user[0].get_user()
            },
            context_instance=RequestContext(request)
        )
    else:
        user.update(
            email=request.POST['email'],
            site=request.POST['site'],
            location=request.POST['location'],
            comment=request.POST['comment'],
        )
        return HttpResponseRedirect('/accounts/profile/' + str(user[0].id))


def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            _username = form.cleaned_data['username']
            _email = request.POST['email']
            User(
                username=_username,
                email=_email
            ).save()
            auth.login(request, user=authenticate(username=form.cleaned_data['username'],
                                                  password=form.cleaned_data['password1']))
            return HttpResponseRedirect('/accounts/profile')
    else:
        form = auth.forms.UserCreationForm()
    return render_to_response('accounts/register.html', {
        'form': form,
    }, context_instance=RequestContext(request))
