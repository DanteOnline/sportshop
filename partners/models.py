from django.db import models


class Partner(models.Model):
    name = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
