from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class LeaveAppUser(AbstractUser):
    pass


# class Leavetype(models.Model):
#     name = models.CharField(max_length=20,blank=False)
#
#     def __str__(self):
#         return self.name
#
#
# class Postleave(models.Model):
#     leavetype = models.ForeignKey(Leavetype, on_delete=models.CASCADE, default=None, null=True)
#     date = models.DateField()
#     email = models.EmailField(max_length=30)
#     reason = models.CharField(max_length=300)
#     contact = models.IntegerField()