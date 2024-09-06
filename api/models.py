from django.db import models

# Create your models here.


class FeedbackMessage(models.Model):
    message = models.TextField()

