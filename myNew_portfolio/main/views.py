from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.core.mail import BadHeaderError

from .models import Profile, Skill, Education, Experience, Service, Project, Social
from .forms import ContactMe


def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    services = Service.objects.all()
    projects = Project.objects.all()
    social = Social.objects.first()
    form = ContactMe(request.POST or None)

    context = {
        'profile': profile,
        'skills': skills,
        'educations': educations,
        'experiences': experiences,
        'services': services,
        'projects': projects,
        'social': social,
        'form': form
    }

    return render(request, 'main/home.html', context)


def contact(request):
    if request.is_ajax():
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            try:
                send_mail(subject, message, email,
                          ['f.benayad95@gmail.com'])
            except BadHeaderError:
                return JsonResponse({
                    'msg': 'Invalid header found.',
                    'type': 'error',
                    'confirmation': 'true',
                })
            return JsonResponse({
                'msg': 'Your email has been sent successfully to Fouad',
                'type': 'success',
                'confirmation': 'true'
            })
        else:
            return JsonResponse({
                'msg': 'Make sure all fields are entered are valid.',
                'type': 'error',
                'confirmation': 'true'
            })


def handle_404(request, exception):
    data = {
        'status_code': "404",
        'error_message': "The link you followed may be broken, or the page may have been removed."
    }
    return render(request, 'error_handler.html', data)


def handle_500(request):
    data = {
        'status_code': "500",
        'error_message': "Server Error, Something went wrong."
    }
    return render(request, 'error_handler.html', data)
