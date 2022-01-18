from django.db import models
from django.utils import timezone
from accounts.models import CustomUser


class Post(models.Model):
    # blank = true -> it is required section, null = true -> attribute in database can be null
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    yourname = models.CharField(max_length=120, null=True)
    title = models.CharField(max_length=120, null=True)
    description = models.TextField(blank=False, null=True)
    dept_name = models.CharField(max_length=120, null=True)
    requirement = models.TextField(blank=False, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    email = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title

'''class DeptList(models.Model):
 
    # fields of the model
    name = models.CharField(max_length = 200)
 
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.name'''