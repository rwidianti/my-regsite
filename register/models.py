from django.db import models

# Create your models here.
class regdata(models.Model):
    nama = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    tlp = models.CharField(max_length=16)

    def __str__(self):
        return self.nama
