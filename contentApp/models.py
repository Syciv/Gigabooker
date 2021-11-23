from datetime import datetime

from django.db import models

#  height_field=300, width_field=300,


class Books(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    author = models.ForeignKey('Authors', on_delete=models.PROTECT, related_name="books")
    information = models.TextField(default='Пока ничего нет')
    img = models.ImageField(upload_to='books',  null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class Authors(models.Model):
    name = models.CharField(max_length=100)
    birth = models.DateField(null=True, blank=True)
    death = models.DateField(null=True, blank=True)
    information = models.TextField(default='Пока ничего нет')
    img = models.ImageField(upload_to='authors', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class Reviews(models.Model):
    name = models.CharField(max_length=100)
    shortReview = models.CharField(max_length=150)
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now())
    target = models.ForeignKey('Books', on_delete=models.CASCADE, related_name="reviews")
