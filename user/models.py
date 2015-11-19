from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(blank=False, max_length=30, unique=True)
    email = models.EmailField(unique=True)
    site = models.TextField()
    location = models.TextField()
    comment = models.TextField()

    def get_user(self):
        user = {
            'username': str(self.username),
            'id': str(self.id)
        }
        return user
