from django.db import models

class Applications(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100, blank=True)
    comment = models.TextField(max_length=500, blank=True)
    create_time = models.DateTimeField(auto_now=True)


