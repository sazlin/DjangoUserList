from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse

from UserListApp.models import User

def index(request):
    user_list = User.objects.all()
    template = loader.get_template('userlist/index.html')
    context = RequestContext(request, {
        'user_list': user_list,
        })
    return HttpResponse(template.render(context))


def add(request):
    newUser = User(first_name=request.POST['firstName'],
                   last_name=request.POST['lastName'],
                   email=request.POST['email'],)
    newUser.save()
    return HttpResponseRedirect(reverse('index'))


def edit(request):
    user = User.objects.get(email=request.POST['originalEmail'])
    if request.POST['submitButton'] == 'Update':
        user.first_name = request.POST['firstName']
        user.last_name = request.POST['lastName']
        user.email = request.POST['email']
        user.save()
    elif request.POST['submitButton'] == 'Delete':
        user.delete()
    
    return HttpResponseRedirect(reverse('index'))
