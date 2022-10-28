from django.db import models

from django.db import models


class Reporter(models.Model):
    first_name = models.CharField(max_lenght=30)
    last_name = models.CharField(max_lenght=30)
    email = models.EmailField()

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

