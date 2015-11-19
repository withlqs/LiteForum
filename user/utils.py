import hashlib


def get_gravatar(email):
    default = "http://www.example.com/default.jpg"
    size = 100
    email_str = email.encode('utf-8')
    gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email_str.lower()).hexdigest() + "?d=" + str(size)
    return str(gravatar_url)
