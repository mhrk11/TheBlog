from django.db import models


class Book(models.Model):
    title=models.CharField(max_length=200)
    reviewer=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    review=models.TextField()


    def __str__(self):
        return self.title

# Create your models here.
