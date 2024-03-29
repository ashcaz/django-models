from django.db import models
from django.contrib.auth import get_user_model


class Snacks(models.Model):
    name = models.CharField(max_length=256)
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name