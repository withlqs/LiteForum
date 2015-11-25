from django.db import models

from liteforum_app.user import utils


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(blank=False, max_length=30, unique=True)
    email = models.EmailField()
    site = models.TextField()
    location = models.TextField()
    comment = models.TextField()


    def get_user(self):
        user = {
            'username': str(self.username),
            'id': str(self.id),
            'email': str(self.email),
            'site': str(self.site),
            'location': str(self.location),
            'comment': str(self.comment),
            'gravatar': utils.get_gravatar(str(self.email)),
            'is_authenticated': True
        }
        return user

    def __str__(self):
        return self.username