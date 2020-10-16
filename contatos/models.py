from django.db import models


class table(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
