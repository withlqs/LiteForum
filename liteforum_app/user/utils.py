import hashlib

from django.contrib.auth.models import User


def get_gravatar(email):
    default = "http://www.example.com/default.jpg"
    size = 60
    email_str = email.encode('utf-8')
    gravatar_url = "http://cdn.v2ex.co/gravatar/" + hashlib.md5(email_str.lower()).hexdigest() + ".jpg?d=retro"
    return str(gravatar_url)


if False:
    User
