from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default=None, null=True, blank=True)
    category = models.CharField(max_length=200, default=None, null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    task = models.TextField(null=True)
    special_requirement = models.TextField(null=True, blank=True)
    file =models.FileField(null=True, blank=True)
    status = models.CharField(max_length=200, default=None, null=True, blank=True)


    def __str__(self):
        return self.title





