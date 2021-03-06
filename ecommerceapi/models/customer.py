from django.db import models
from django.db.models import F
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    phone_number = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # class Meta:
    #     ordering = (F('user.date_joined').asc(nulls_last=True),)
