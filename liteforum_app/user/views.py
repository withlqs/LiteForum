from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth import forms
from django.contrib.auth import views
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from liteforum_app.user.models import User
from . import utils

# Create your views here.

admin_name = 'administrator'


def logged(request):
    return HttpResponseRedirect('/')


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
    return render(
        request,
        'success.html',
        # context_instance=RequestContext(request)
    )


def login(request):
    if request.user.is_authenticated():
        if request.user.get_username() == admin_name:
            return HttpResponseRedirect('/manage/')
        return HttpResponseRedirect('/')
    return views.login(request, template_name='accounts/login.html')


def profile(request, user_id):
    print('id:' + user_id)
    user = User.objects.get(id=user_id)
    if user is None:
        return Http404
    editable = False
    if request.user.is_authenticated():
        editable = (request.user.get_username() == str(user.username))

    tlist = user.topic_set.order_by('-pub_date')
    rlist = user.reply_set.order_by('-pub_date')

    return render(
        request,
        'accounts/profile.html',
        {
            'user': user.get_user(),
            'editable': editable,
            'rlist': rlist,
            'tlist': tlist,
            'tcount': len(tlist),
            'rcount': len(rlist),
        }
    )


def profile_edit(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    user = utils.User.objects.filter(username=request.user.get_username())
    user_info = User.objects.filter(username=request.user.get_username())
    if request.method == 'GET':
        return render(
            request,
            'accounts/profile_edit.html',
            {
                'user': user_info[0].get_user(),
                'new_password_error': None,
                'password_error': None,
            },
            # context_instance=RequestContext(request)
        )
    else:
        # authentication = authenticate(username=request.user.get_username(), password=request.POST['password'])
        # print('#' + request.user.get_username() + '#' + request.POST['password'])
        # if authentication is not None:
        if request.POST['password1'] == request.POST['password2']:
            if request.POST['password1'] != '':
                user[0].set_password(request.POST['password1'])
                user[0].save()
            user_info.update(
                email=request.POST['email'],
                site=request.POST['site'],
                location=request.POST['location'],
                comment=request.POST['comment'],
            )
            return HttpResponseRedirect('/accounts/profile/' + str(user[0].id))
        else:
            return render(
                request,
                'accounts/profile_edit.html',
                {
                    'user': request.POST,
                    'new_password_error': '*Repeat Password Do NOT Match',
                    'password_error': None,
                },
                # context_instance=RequestContext(request)
            )

            # else:
            #     return render_to_response(
            #         'accounts/profile_edit.html',
            #         {
            #             'user': request.POST,
            #             'new_password_error': None,
            #             'password_error': '*Password Do NOT Match!',
            #         },
            #         context_instance=RequestContext(request)
            #     )


def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            _username = form.cleaned_data['username']
            _email = request.POST['email']
            print(User.objects.all().count())
            if User.objects.all().count() < utils.User.objects.all().count():
                admin = utils.User.objects.all()[0]
                User(
                    username=admin.username,
                    email=admin.email
                ).save()
            User(
                username=_username,
                email=_email
            ).save()
            form.save()
            auth.login(request, user=authenticate(username=form.cleaned_data['username'],
                                                  password=form.cleaned_data['password1']))
            return HttpResponseRedirect('/')
    else:
        form = auth.forms.UserCreationForm()
    return render(
        request,
        'accounts/register.html', {
            'form': form,
        },
        # context_instance=RequestContext(request)
    )
