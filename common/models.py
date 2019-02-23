from django.db import models


# Create your models here.


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Nameable(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        abstract = True


class Active(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
