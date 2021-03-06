from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils import timezone


class Project(models.Model):
    name = models.CharField(max_length=100)
    budget = models.IntegerField()
    description = models.TextField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # one to many
    image = models.ImageField(
        default='default-project.jpg', upload_to='project_pics')
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     middle_name = models.CharField(max_length=30, blank=True)
#     dob = models.DateField(null=True, blank=True)
