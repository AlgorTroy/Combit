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
<<<<<<< HEAD
from JobApp.models import Job
=======
from django.contrib import messages
>>>>>>> 30cd2418c8754f66c9285977466e9b6a6e7d352a

# redirect = ''

def home(request):
    # CHANGED to new home just add home.html at any error

    crsl_images = [static('img/carousel/home-bg.jpg'),
                   static('img/carousel/home-bg.jpg'),
                   static('img/carousel/contact-bg.jpg')]

    tag_lines = ['Organize Events',
                 'Find Part-Time Jobs',
                 'Connect with People']
    jobs = Job.objects.all().order_by('-created_at')[:5]
    return render(request,
                  'home.html',
                  {'crsl_images': crsl_images,
                   'tag_lines': tag_lines,
                    'recent_jobs': jobs})

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
                    to_redirect = request.session['next']
                    del request.session['next']
                    if to_redirect == '':
                        to_redirect = '/'

                    return HttpResponseRedirect(to_redirect, {'user': user})
                else:
                    messages.error(request, 'Disabled Account!!')
                    return redirect("/")
            else:
                messages.error(request, 'Invalid Login!!')
                return redirect("/")
    else:
        to_redirect = request.GET.get('next', '')
        request.session['next'] = to_redirect
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})
