from django.db import models


# Create your models here.

class visitors(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name


class contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.email


class visitormails(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
