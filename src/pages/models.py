from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    # blank = true -> it is required section, null = true -> attribute in database can be null
    yourname = models.CharField(max_length=120, null=True)
    title = models.CharField(max_length=120, null=True)
    description = models.TextField(blank=True, null=True)
    dept_name = models.CharField(max_length=120, null=True)
    requirement = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title