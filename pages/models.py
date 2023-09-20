from django.db import models


class About(models.Model):
    name = models.CharField(max_length=128, default="edgar")

    def __str__(self):
        return self.title
