import logging
import datetime

from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.conf import settings

from .forms import SearchForm
from .models import Page


def index(request):
    logger = logging.getLogger('search_logger')
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data['search_term']
            email = form.cleaned_data['email']

            start_time = datetime.datetime.now()
            logger.info("Start search, " + str(start_time))

            pages = Page.objects.filter(text__icontains=search_term)

            end_time = datetime.datetime.now()
            logger.info("End search, " + str(end_time))
            logger.info('Time of searching: ' + str(end_time-start_time))

            html = get_template('mail.html')
            d = Context({'pages': pages, 'search_term': search_term})
            subject, from_email, to = 'Search result',\
                                      settings.EMAIL_HOST_USER,\
                                      email
            text_content = "Search results"
            html_content = html.render(d)

            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            return HttpResponse(
                'Search was started, results will sent on ' + email
            )
    else:
        form = SearchForm()
    return render(request, 'main.html', {"form": form})
