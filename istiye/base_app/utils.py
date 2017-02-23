__author__ = 'Hakan Uyumaz'

import random

from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import urllib


def generate_token():
    activation_key = str(random.random()).encode('utf8')
    return activation_key


def send_activation_mail(user):
    subject = "Activate your Sophist Journey Account"
    body = """Hello {0} {1},
Thank you for signing up for Medically.
Please click the link below to activate your account:
http://127.0.0.1:8000/activate/{2}/
Best Regards,
Sophist Journey
            """.format(user.name, user.surname, user.activation_key)

    mail = EmailMessage(subject, body, "Sophist Journey <hakanuyumaz@gmail.com>", to=[user.email])
    mail.send(fail_silently=False)
    response = mail.mandrill_response[0]


def send_activation_successful_mail(user):
    subject = "Your Sophist Journey Account is Now Active!"
    body = """Hello {0} {1},
Thank you for signing up for Sophist Journey.
You have now successfully activated your account.
Best Regards,
Sophist Journey
        """.format(user.name, user.surname)

    mail = EmailMessage(subject, body, "Sophist Journey <hakanuyumaz@gmail.com>", to=[user.email])
    mail.send(fail_silently=False)

def custom_redirect(url_name, *args, **kwargs):
    url = reverse(url_name, args = args)
    params = urllib.parse.urlencode(kwargs)
    return HttpResponseRedirect(url + "?%s" % params)
