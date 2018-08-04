from django.db import models

# Create your models here.
class List(models.Model):
    item = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, default='')
    title = models.CharField(max_length=256, default='')
    author = models.CharField(max_length=256, default='')
    genre = models.CharField(max_length=256, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)



    def __str__(self):
        return self.title
