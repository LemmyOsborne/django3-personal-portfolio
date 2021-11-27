from django.db import models
from datetime import date

class Blog(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    published_date = models.DateField(default=date.today)

    def __str__(self):
        return self.title
