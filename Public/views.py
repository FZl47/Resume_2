from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.views import View
from MyResume import Tools
from . import models


def get_information_obj():
    return models.Information.objects.first()

@cache_page(settings.CACHES_TIMEOUT)
def index(request):
    context = {
        'information': get_information_obj(),
        'certificates': models.Certificate.objects.all(),
        'reviews': models.Review.objects.filter(is_showing=True).all()
    }

    return render(request, 'Public/index.html', context)

@cache_page(settings.CACHES_TIMEOUT)
def resume(request):
    context = {
        'information': get_information_obj(),
        'experiences': models.Experience.objects.all(),
        'educations': models.Education.objects.all(),
        'skills': models.Skill.objects.filter(is_showing=True).all()
    }
    return render(request, 'Public/resume.html', context)

@cache_page(settings.CACHES_TIMEOUT)
def worksamples(request):
    context = {
        'information': get_information_obj(),
        'worksamples': models.WorkSample.objects.all(),
        'skills': models.Skill.objects.all()
    }
    return render(request, 'Public/work-samples.html', context)

@cache_page(settings.CACHES_TIMEOUT)
def worksample_detail(request, slug):
    worksample = models.WorkSample.objects.get_by_slug(slug)
    if not worksample:
        return redirect('Public:worksamples')
    worksample.views += 1
    worksample.save()
    context = {
        'information': get_information_obj(),
        'worksample': worksample
    }
    return render(request, 'Public/work-sample-detail.html', context)


class contact(View):
    template_name = 'Public/contact.html'

    def get(self, request):
        contact_me_is_sended = True if (request.COOKIES.get('contact-me-sended') or None) else False
        context = {
            'information': get_information_obj(),
            'contact_me_is_sended': contact_me_is_sended
        }
        return render(request, self.template_name, context)

    def post(self, request):
        data = request.POST
        name = data.get('name') or None
        email = data.get('email') or None
        message = data.get('message') or None
        email_valid = False
        try:
            validate_email(email)
            email_valid = True
        except ValidationError:
            email_valid = False

        url_redirect = reverse('Public:contact_me')
        if name and email_valid and message:
            models.Contact.objects.create(name=name, email=email, message=message)
            response = HttpResponseRedirect(url_redirect)
            response = Tools.Set_Cookie(response, 'contact-me-sended', True, 0.0008)
            return response
        return HttpResponseRedirect(url_redirect)


class review(View):
    template_name = 'Public/review.html'

    def get(self, request):
        review_sended = True if (request.COOKIES.get('review-sended') or None) else False
        context = {
            'information': get_information_obj(),
            'avatars':settings.AVATARS_SRC,
            'review_sended': review_sended
        }
        return render(request, self.template_name, context)

    def post(self, request):
        data = request.POST
        name = data.get('name') or None
        description = data.get('description') or None
        avatar = data.get('avatar') or None

        url_redirect = reverse('Public:review')
        if name and avatar and description:
            models.Review.objects.create(name=name, description=description,image=avatar)
            response = HttpResponseRedirect(url_redirect)
            response = Tools.Set_Cookie(response, 'review-sended', True, 1000)
            return response
        return HttpResponseRedirect(url_redirect)


def clear_cache(request):
    cache.clear()
    return HttpResponse('Cache Cleared Successfully')