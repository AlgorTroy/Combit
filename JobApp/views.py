from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from .forms import JobUploadForm
from .models import Category, Job, Application
from django.core.paginator import Paginator, EmptyPage,\
PageNotAnInteger
from django.contrib import messages
from django.core.mail import send_mail


@login_required
def upload_job(request):

    if request.method == 'POST':

        form = JobUploadForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.status = 'open'
            job.user = request.user
            job.save()
            messages.success(request, 'Job posted successfully!!')
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Unable to upload job! Retry')
            return redirect(request.path)
    else:
        form = JobUploadForm()
        return render(request, 'job/upload.html', {'form': form})


def jobs_by_category(request, slug):
    jobs = Job.objects.filter(category__slug=slug)
    paginator = Paginator(jobs, 8)
    page = request.GET.get('page')
    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        jobs = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        jobs = paginator.page(paginator.num_pages)

    return render(request, 'job/by_filter.html', {'page': page, 'jobs': jobs})

def jobs_by_user(request, username):
    jobs = Job.objects.filter(user__username=username)
    paginator = Paginator(jobs, 8)
    page = request.GET.get('page')
    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        jobs = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        jobs = paginator.page(paginator.num_pages)

    return render(request, 'job/by_filter.html', {'page': page, 'jobs': jobs})

def recent_jobs(request):
    jobs = Job.objects.all().order_by('-created_at')[:5]

    return render(request, 'home.html', {'recent_jobs': jobs})


def jobs_by_type(request, job_type):
    jobs = Job.objects.filter(type=job_type)

    paginator = Paginator(jobs, 8)
    page = request.GET.get('page')
    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        jobs = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        jobs = paginator.page(paginator.num_pages)

    return render(request, 'job/by_filter.html', {'page': page, 'jobs': jobs})


def search_engine(request):
    pass


def apply_job(request, job_id):
    job = Job.objects.get(id=job_id)
    if job.status == 'open':
        application = Application.objects.filter(user=request.user, job=job)
        if not application:
            application = Application()
            application.user = request.user
            application.job = job
            application.status = 'applied'
            application.save()
            # notify_with_email(job.user)
            messages.success(request, 'Successfully applied to job: '+job.title)
            return redirect(request.path)

        else:
            messages.error(request, 'You have already applied to this job!!')
            return redirect(request.path)
    elif job.status == 'closed':
        messages.error(request, 'This job is closed!!')
        return redirect(request.path)
    else:
        messages.error(request, 'Oops!! This job is already taken')
        return redirect(request.path)


def notify_with_email(user):

    send_mail(
    'Subject here',
    'Here is the message.',
    'azurathena@gmail.com',
    [user.email],
    fail_silently=False,
    )
