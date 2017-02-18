from django.shortcuts import render
from MainApp.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.staticfiles.templatetags.staticfiles import static


# redirect = ''

def home(request):
    # CHANGED to new home just add home.html at any error

    crsl_images = [static('img/carousel/home-bg.jpg'),
                   static('img/carousel/home-bg.jpg'),
                   static('img/carousel/contact-bg.jpg')]

    tag_lines = ['Organize Events',
                 'Find Part-Time Jobs',
                 'Connect with People']

    return render(request, 'newMaterialHome.html', {'crsl_images': crsl_images,
                                                    'tag_lines': tag_lines})

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            user.save()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


def user_login(request):
    # global redirect

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
            password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    redirect = request.session['next']
                    del request.session['next']

                    print('==================', request.GET.get('next'))
                    return HttpResponseRedirect(redirect, {'user': user})
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        redirect = request.GET.get('next')
        request.session['next'] = redirect
        print('this?', redirect)
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})
