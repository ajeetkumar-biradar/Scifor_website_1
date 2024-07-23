from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from carrer import models
from carrer import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import View
from .forms import JobForm, ApplicationForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Testimonial, CaseStudy, Article
import csv


# Existing views

def carrer(request):
    return render(request, 'carrer/carrer.html')


def main(request):
    return render(request, 'carrer/jobsPage.html')


def jobsPgae(request, call="No"):
    data = []
    objs = models.Jobs.objects.all()
    for i in objs:
        data.append(i.educationLevel)
    return render(request, 'carrer/jobsPage.html', context={'levels': data, 'call': call})


class getAllJobs(APIView):
    def get(self, request, *args, **kwargs):
        data = []
        objs = models.Jobs.objects.all()
        for i in objs:
            data.append(serializers.JobSerializer(i).data)
        return Response(data)


class getJob(APIView):
    def get(self, request, *args, **kwargs):
        _id = request.GET.get('id')
        obj = models.Jobs.objects.get(id=_id)
        print(serializers.JobSerializer(obj).data)
        return Response(dict(serializers.JobSerializer(obj).data))


class ApplicationView(View):
    def post(self, request, *args, **kwargs):
        obj = models.Application(resume=request.FILES.get('resume'),
                                 name=request.POST.get('name'), mob=request.POST.get('mobile'),
                                 mailID=request.POST.get('email'),
                                 job=models.Jobs.objects.get(id=request.POST.get('id')))
        obj.save()
        return jobsPgae(request, call="yes")


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'carrer/admin_login.html')


@login_required
def admin_logout(request):
    logout(request)
    return redirect('admin_login')


# Custom admin views
def admin_dashboard(request):
    return render(request, 'carrer/admin_dashboard.html')


def admin_job_list(request):
    jobs = models.Jobs.objects.all()
    return render(request, 'carrer/admin_job_list.html', {'jobs': jobs})


def admin_job_add(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_job_list')
    else:
        form = JobForm()
    return render(request, 'carrer/admin_job_form.html', {'form': form})


def admin_job_edit(request, pk):
    job = get_object_or_404(models.Jobs, pk=pk)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('admin_job_list')
    else:
        form = JobForm(instance=job)
    return render(request, 'carrer/admin_job_form.html', {'form': form})


def admin_job_delete(request, pk):
    job = get_object_or_404(models.Jobs, pk=pk)
    if request.method == 'POST':
        job.delete()
        return redirect('admin_job_list')
    return render(request, 'carrer/admin_job_confirm_delete.html', {'job': job})


def admin_application_list(request):
    applications = models.Application.objects.all()
    return render(request, 'carrer/admin_application_list.html', {'applications': applications})


def admin_application_add(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_application_list')
    else:
        form = ApplicationForm()
    return render(request, 'carrer/admin_application_form.html', {'form': form})


def admin_application_edit(request, pk):
    application = get_object_or_404(models.Application, pk=pk)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES, instance=application)
        if form.is_valid():
            form.save()
            return redirect('admin_application_list')
    else:
        form = ApplicationForm(instance=application)
    return render(request, 'carrer/admin_application_form.html', {'form': form})


def admin_application_delete(request, pk):
    application = get_object_or_404(models.Application, pk=pk)
    if request.method == 'POST':
        application.delete()
        return redirect('admin_application_list')
    return render(request, 'carrer/admin_application_confirm_delete.html', {'application': application})


def send_admin_email(name, email, phone, inquiry):
    subject = 'New Inquiry'
    message = f"New inquiry received:\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nInquiry: {inquiry}"
    recipient_list = ['justfun1394@gmail.com']
    send_mail(subject, message, EMAIL_HOST_USER, recipient_list)


def send_acknowledgment_email(name, email):
    subject = 'Thank You for Your Inquiry'
    message = f"Dear {name},\n\nThank you for reaching out to us. We have received your inquiry and will get back to you shortly.\n\nBest regards,\n Meta Scifor Technologies"
    recipient_list = [email]
    send_mail(subject, message, EMAIL_HOST_USER, recipient_list)


def home(request):
    testimonials = Testimonial.objects.all()
    case_studies = CaseStudy.objects.all()
    return render(request, 'carrer/page.html', {'testimonials': testimonials, 'case_studies': case_studies})


def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        inquiry = request.POST.get('inquiry')
        send_acknowledgment_email(name, email)
        send_admin_email(name, email, phone, inquiry)
        return redirect('thank_you', name=name)


def inquiry_form(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email_')
        industry = request.POST.get('industry')
        expert_inquiry = request.POST.get('expert_inquiry')
        send_acknowledgment_email(firstname + ' ' + lastname, email)
        send_admin_email(firstname + ' ' + lastname, email, '', industry + ': ' + expert_inquiry)
        return redirect('thank_you', name=firstname)



def case_study(request):
    case_studies = CaseStudy.objects.all()
    return render(request, 'carrer/case_study.html', {'case_studies': case_studies})


def web_service(request):
    return render(request, 'carrer/services.html')


def community_engagement_page(request):
    category = request.GET.get('category', 'TECH BLOGS')
    latest_articles = Article.objects.all().order_by('-created_on')[:5]
    articles = Article.objects.filter(category=category)
    context = {
        'latest_articles': latest_articles,
        'articles': articles,
        'active_category': category,
    }
    return render(request, 'carrer/community_engagement_page.html', context)


def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    context = {
        'article': article,
    }
    return render(request, 'carrer/article_detail.html', context)


def get_in_touch(request):
    return render(request, 'carrer/get_in_touch.html')


def achievements(request):
    return render(request, 'carrer/achievements.html')


def about_company(request):
    return render(request, 'carrer/about_company.html')


def company_name(request):
    return render(request, 'carrer/company_name.html')


def who_are_we(request):
    return render(request, 'carrer/who_are_we.html')


def about_us_page(request):
    return render(request, 'carrer/about_us_page.html')


def team_profiles(request):
    return render(request, 'carrer/team_profiles.html')


def software_development(request):
    return render(request, 'carrer/software_development.html')


def devops_services(request):
    return render(request, 'carrer/devops.html')


def game_development(request):
    return render(request, 'carrer/game_development.html')


def ui_ux_design(request):
    return render(request, 'carrer/ui_ux_design.html')
